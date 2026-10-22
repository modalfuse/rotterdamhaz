"""Fit the OD scale (total tons) and the gateway share of a region to observed link counts (RotterdamHaz: RWS VGS), with a light build
(population exposure for one small radius only; OD, AON assignment and calibration_sites as in hazbench.build).
  python scripts/fit_od_totals.py regions/<region>.yaml <work_dir> share1,share2,...
For each gateway share: model flows scale linearly with the total, so the total that gives median(model/observed) = 1 for class3 over the
matched sites with observed > 0 and model > 0 is total_base * 1/median; the share with the smallest median |log(model/observed)| (class3 and class2
pooled, after rescaling) is reported. Writes <work_dir>/fit_od_totals.csv."""
import sys, shutil, tempfile
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hazbench.config import load
from hazbench.build import Build

cfg, work, shares = sys.argv[1], Path(sys.argv[2]).resolve(), [float(x) for x in sys.argv[3].split(",")]
work.mkdir(parents=True, exist_ok=True); rows = []
R0 = load(cfg); rad = pd.read_csv(R0.path("radii")); small = work / "radii_small.csv"
rad[rad.substance == rad.sort_values("primary_radius_km").substance.iloc[0]].to_csv(small, index=False)
for g in shares:
    R = load(cfg, [f"radii={small}"]); R["P"]["gateway_share"] = g
    out = work / f"fit_g{g}"; shutil.rmtree(out, ignore_errors=True)
    b = Build(R, out); b.network(); b.population(); b.facilities(); b.od()
    c = pd.read_csv(out / "calibration_sites.csv"); m = c[c.arcs.notna()]
    tot = R["P"]["od_totals_10kt"]["total"]["base"]
    r3 = (m.model_before_class3 / m.obs_class3)[m.obs_class3 > 0]; f = 1 / np.median(r3[r3 > 0])   # sites on modelled paths only (through-traffic sites have model 0)
    r2 = (m.model_before_class2 / m.obs_class2)[m.obs_class2 > 0] * f
    lr = np.abs(np.log(np.r_[(r3 * f)[r3 > 0], r2[r2 > 0]])); zero = int((r3 == 0).sum() + (r2 == 0).sum())
    rows.append(dict(gateway_share=g, total_base_fit_10kt=round(tot * f, 1), class3_median_ratio_after_scaling=1.0, class2_median_ratio_after_scaling=float(np.median(r2)),
                     median_abs_log_ratio=float(np.median(lr)), sites_model_zero=zero, n_sites=len(m)))
    print(rows[-1])
pd.DataFrame(rows).to_csv(work / "fit_od_totals.csv", index=False); print(pd.DataFrame(rows).to_string())
