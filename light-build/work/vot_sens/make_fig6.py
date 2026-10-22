"""Fig 6 VoT sweep: python make_fig6.py <out.pdf>"""
import sys, pandas as pd, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from pathlib import Path
d = pd.read_csv(Path(__file__).parent / "run/sens_od_summary.csv"); t = d[d.variant != "no_toll"]
f = [float(v.split("x")[1]) for v in t.variant]
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].plot(f, t.Z152_class3_ratio_before, "o-", c="k", label="Z152 before cal."); ax[0].axhline(d.Z152_class3_ratio_before.iloc[-1], ls=":", c="grey", label="no toll")
ax[0].axhline(1, c="grey", lw=.5); ax[0].axvline(1, ls="--", c="r", lw=.8); ax[0].set_xscale("log"); ax[0].set_xlabel("VoT / KiM value"); ax[0].set_ylabel("class 3 model/observed"); ax[0].legend(fontsize=7)
ax[1].plot(f, t.class3_ratio_before_median, "o-", label="median ratio class 3"); ax[1].plot(f, t.class3_GEH_after_median / 10, "s-", label="median GEH after /10"); ax[1].plot(f, t.total_cal_10kt / 904.1, "^-", label="cal. total / base")
ax[1].axvline(1, ls="--", c="r", lw=.8); ax[1].set_xscale("log"); ax[1].set_xlabel("VoT / KiM value"); ax[1].legend(fontsize=7)
plt.tight_layout(); plt.savefig(sys.argv[1])
