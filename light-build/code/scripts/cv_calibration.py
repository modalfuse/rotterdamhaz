"""Cross-validation of the VGS calibration (RotterdamHaz 1.0.0, review major comment 3).
Light build (one small exposure radius, as scripts/fit_od_totals.py), gravity OD and AON paths once; then the calibration
(hazbench.calibrate.run) is repeated with held-out count sections removed from the targets (cfg exclude_sites), and the
calibrated model flow on the held-out sections is compared with the observation they did not see.
  python scripts/cv_calibration.py regions/<region>.yaml <work_dir> [n_proc]
Folds: (a) leave-one-section-out over all matched sections; (b) leave-one-road-out (VGS column `road`, e.g. R4 = A4, R15 = A15).
Writes <work_dir>/cv_loo.csv, cv_road.csv (one row per held-out section and class) and cv_summary.csv."""
import sys, copy, shutil, os
from pathlib import Path
from multiprocessing import Pool
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hazbench.config import load
from hazbench.build import Build
from hazbench import calibrate

cfg, work = sys.argv[1], Path(sys.argv[2]).resolve(); NP = int(sys.argv[3]) if len(sys.argv) > 3 else 6
work.mkdir(parents=True, exist_ok=True)
R0 = load(cfg); rad = pd.read_csv(R0.path("radii")); small = work / "radii_small.csv"
rad[rad.substance == rad.sort_values("primary_radius_km").substance.iloc[0]].to_csv(small, index=False)
R = load(cfg, [f"radii={small}"]); b = Build(R, work / "_full"); b.network(); b.population(); b.facilities(); b.od()   # full calibration (all sections)
C0 = R["od"]["calibration"]; obs = pd.read_csv(R.resolve(C0["observed"])); sid = C0["site_id"]
full = pd.read_csv(work / "_full/calibration_sites.csv"); matched = full[full.arcs.notna()].site.tolist()
CLS = C0["class_columns"]

def fold(args):
    name, hold = args
    out = work / "folds" / name; out.mkdir(parents=True, exist_ok=True)
    c = copy.deepcopy(C0); c["exclude_sites"] = list(hold); b.OUT = out
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()): calibrate.run(b, c)
    r = pd.read_csv(out / "calibration_sites.csv"); r = r[r.site.isin(hold)]; rows = []
    for _, x in r.iterrows():
        for hc in CLS:
            ob = float(full.loc[full.site == x.site, f"obs_{hc}"].iloc[0])
            rows.append(dict(fold=name, site=x.site, cls=hc, obs=ob, model_before=x[f"model_before_{hc}"], model_heldout=x[f"model_after_{hc}"],
                             model_insample=float(full.loc[full.site == x.site, f"model_after_{hc}"].iloc[0])))
    for f in ("od_base_calibrated.csv",): (out / f).unlink(missing_ok=True)
    return rows

def geh(m, c): return np.sqrt(2 * (m - c) ** 2 / np.maximum(m + c, 1e-9))
if __name__ == "__main__":
    roads = obs[obs[sid].isin(matched)].groupby("road")[sid].apply(list).to_dict()
    jobs = [(f"loo_{s}", [s]) for s in matched] + [(f"road_{k}", v) for k, v in roads.items()]
    with Pool(NP) as p: res = p.map(fold, jobs)
    df = pd.DataFrame([r for rr in res for r in rr])
    for c in ("before", "heldout", "insample"):
        df[f"GEH_{c}"] = geh(df[f"model_{c}" if c != "before" else "model_before"], df.obs).round(2)
        df[f"ratio_{c}"] = np.where(df.obs > 0, df[f"model_{c}" if c != "before" else "model_before"] / df.obs.where(df.obs > 0), np.nan)
    df["road"] = df.site.map(obs.set_index(sid)["road"])
    loo, rd = df[df.fold.str.startswith("loo_")], df[df.fold.str.startswith("road_")]
    loo.to_csv(work / "cv_loo.csv", index=False); rd.to_csv(work / "cv_road.csv", index=False)
    S = []
    for name, d in (("loo", loo), ("road", rd)):
        for hc in CLS:
            x = d[(d.cls == hc) & (d.obs > 0)]
            S.append(dict(scheme=name, cls=hc, n=len(x), GEH_before_median=x.GEH_before.median(), GEH_heldout_median=x.GEH_heldout.median(), GEH_insample_median=x.GEH_insample.median(),
                          GEH_heldout_lt5_share=(x.GEH_heldout < 5).mean(), GEH_heldout_lt10_share=(x.GEH_heldout < 10).mean(),
                          absLogRatio_before_median=np.abs(np.log(x.ratio_before[x.ratio_before > 0])).median(),
                          absLogRatio_heldout_median=np.abs(np.log(x.ratio_heldout[x.ratio_heldout > 0])).median(),
                          ratio_heldout_median=x.ratio_heldout.median(), ratio_heldout_q1=x.ratio_heldout.quantile(.25), ratio_heldout_q3=x.ratio_heldout.quantile(.75),
                          sites_model_zero_heldout=int((x.model_heldout <= 0).sum())))
    S = pd.DataFrame(S); S.to_csv(work / "cv_summary.csv", index=False); print(S.to_string())
