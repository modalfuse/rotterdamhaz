"""Value-of-time sweep for the RotterdamHaz light build.

hazbench comes from code/rotterdamhaz-code-v1.0.1.tgz in the data package and must already be on PYTHONPATH.
The downloaded package does not include OD matrices of 5 MB or larger, so this script cannot be rerun from the package alone.
Light build (one small exposure radius, as scripts/fit_od_totals.py): network, population and facilities are built once, then the OD,
all-or-nothing assignment and VGS calibration are redone for each value of time.
"""
import sys, copy, shutil
from pathlib import Path
import numpy as np, pandas as pd
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
FAC = [0.5, 0.75, 0.95, 1.0, 1.05, 1.25, 1.5, 2.0, 3.0]
V = {f"vot_x{k:g}": (lambda k: (lambda P: P.update(vot_truck_eur_h=P["vot_truck_eur_h"] * k)))(k) for k in FAC}
V["no_toll"] = lambda P: P.update(vot_truck_eur_h=1e12)
TM0 = b.arcs["toll_min"].copy() if "toll_min" in b.arcs else None
rows = []
for name, f in V.items():
    P = copy.deepcopy(P0); f(P); P["beta_sens"] = [P["beta"]]; b.P = R["P"] = P
    out = work / name; shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True); b.OUT = out
    if TM0 is not None:   # v1.0.0: toll as generalized time depends on the VoT -> rescale toll_min and rebuild the routing graphs
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
    z = c.set_index("site").loc["Z152"] if "site" in c.columns else c.set_index(c.columns[0]).loc["Z152"]
    r["vot_eur_h"] = round(P["vot_truck_eur_h"], 2) if P["vot_truck_eur_h"] < 1e9 else float("inf")
    r["toll_min"] = round(60 * P0["tolls"][0]["toll_eur"] / P["vot_truck_eur_h"], 2)
    for hc in ("class3", "class2"):
        r[f"Z152_{hc}_ratio_before"] = round(float(z[f"model_before_{hc}"] / z[f"obs_{hc}"]), 3) if z[f"obs_{hc}"] > 0 else None
        r[f"Z152_{hc}_ratio_after"] = round(float(z[f"model_after_{hc}"] / z[f"obs_{hc}"]), 3) if z[f"obs_{hc}"] > 0 else None
        r[f"Z152_{hc}_GEH_after"] = round(float(z[f"GEH_after_{hc}"]), 1)
    rows.append(r); print(r, flush=True)
pd.DataFrame(rows).to_csv(work / "sens_od_summary.csv", index=False); print(pd.DataFrame(rows).to_string())
