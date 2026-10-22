"""OD sensitivity runs for RotterdamHaz (v0.3 items 2 and 4): class-2 share, refinery/port/chemical allocation and beta.
Light build (one small exposure radius, as scripts/fit_od_totals.py); network, population and facilities are built once, then the OD,
AON assignment and VGS calibration are redone per variant.
  python scripts/sens_od.py regions/<region>.yaml <work_dir>
Writes <work_dir>/<variant>/{od_base.csv, od_base_calibrated.csv, calibration_sites.csv} and <work_dir>/sens_od_summary.csv with, per variant:
OD total, class shares (gravity and calibrated), model/observed median ratio and median GEH before / after calibration per class."""
import sys, copy, shutil
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hazbench.config import load
from hazbench.build import Build

cfg, work = sys.argv[1], Path(sys.argv[2]).resolve(); work.mkdir(parents=True, exist_ok=True)
R0 = load(cfg); rad = pd.read_csv(R0.path("radii")); small = work / "radii_small.csv"
rad[rad.substance == rad.sort_values("primary_radius_km").substance.iloc[0]].to_csv(small, index=False)
R = load(cfg, [f"radii={small}"]); P0 = copy.deepcopy(R["P"])
b = Build(R, work / "_common"); b.network(); b.population(); b.facilities()

def split(P, port=1.0, ref=1.0):   # scale the port / refinery allocation; the chemical remainder absorbs the change (total fixed)
    O = P["od_totals_10kt"]
    for sc in ("low", "base", "high"): O["port"][sc] = round(O["port"][sc] * port, 1); O["refinery"][sc] = round(O["refinery"][sc] * ref, 1)
def c2(P, v):
    for t in P["class_split"].values(): t["class3"] = round(1 - v - t["other"], 4); t["class2"] = v
V = {"base": lambda P: None,
     "class2_0.09": lambda P: c2(P, P["class_split_sens"]["class2"]),
     "beta_1.5": lambda P: P.update(beta=1.5), "beta_2.5": lambda P: P.update(beta=2.5),
     "port_x0.5": lambda P: split(P, port=0.5), "port_x1.5": lambda P: split(P, port=1.5),
     "refinery_x0.5": lambda P: split(P, ref=0.5), "refinery_x1.5": lambda P: split(P, ref=1.5),
     "vot_x1.5": lambda P: P.update(vot_truck_eur_h=P["vot_truck_eur_h"] * P.get("vot_sens_factor", [1.5])[0])}   # 1.0.0: hazmat VoT x 1.5 (toll weight / 1.5)
TM0 = b.arcs["toll_min"].copy() if "toll_min" in b.arcs else None
rows = []
for name, f in V.items():
    P = copy.deepcopy(P0); f(P); P["beta_sens"] = [P["beta"]]; b.P = R["P"] = P
    out = work / name; shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True); b.OUT = out
    if TM0 is not None:   # 1.0.0: toll as generalized time depends on the VoT -> rescale toll_min and rebuild the routing graphs
        fv = P0["vot_truck_eur_h"] / P["vot_truck_eur_h"]
        if abs(fv - 1) > 1e-9 or not b.arcs["toll_min"].equals(TM0):
            b.arcs["toll_min"] = (TM0 * fv).round(4); b.OUT = work / "_common"; b.facilities(); b.OUT = out
    b.od()
    c = pd.read_csv(out / "calibration_sites.csv"); oc = pd.read_csv(out / "od_base_calibrated.csv"); og = b.ods["base"]
    r = dict(variant=name, total_10kt=round(og.tons_per_year.sum() / 1e4, 1), total_cal_10kt=round(oc.tons_per_year.sum() / 1e4, 1))
    for hc in ("class3", "class2"):
        m = c[c.arcs.notna() & (c[f"obs_{hc}"] > 0)]
        r[f"{hc}_share_gravity"] = round(og[og.hazmat_class == hc].tons_per_year.sum() / og.tons_per_year.sum(), 3)
        r[f"{hc}_share_cal"] = round(oc[oc.hazmat_class == hc].tons_per_year.sum() / oc.tons_per_year.sum(), 3)
        r[f"{hc}_ratio_before_median"] = round(float((m[f"model_before_{hc}"] / m[f"obs_{hc}"]).median()), 3)
        r[f"{hc}_ratio_after_median"] = round(float((m[f"model_after_{hc}"] / m[f"obs_{hc}"]).median()), 3)
        r[f"{hc}_GEH_before_median"] = round(float(m[f"GEH_before_{hc}"].median()), 1); r[f"{hc}_GEH_after_median"] = round(float(m[f"GEH_after_{hc}"].median()), 1)
    rows.append(r); print(r, flush=True)
pd.DataFrame(rows).to_csv(work / "sens_od_summary.csv", index=False); print(pd.DataFrame(rows).to_string())
