# RotterdamHaz: an open benchmark dataset for hazmat road transport risk

> STATUS: 1.0.1, repository https://github.com/modalfuse/rotterdamhaz. Dataset DOI: https://doi.org/10.5281/zenodo.23568109.

## Description
RotterdamHaz is an open benchmark for hazardous-materials (hazmat) road transport risk in the Rotterdam–Rijnmond
port and industrial area (Pernis, Botlek, Europoort, Maasvlakte and the surrounding Rijnmond urban area), the Netherlands.
It contains a directed road network (EPSG:28992) with per-arc release frequencies, ADR tunnel restrictions and an A24 toll
as generalized time; 100 m night/day population exposure rasters and per-substance arc–cell exposure matrices
(benzene, LPG, ammonia, chlorine; ERG 2024 radii); facility (generation/attraction) points and gateways; gravity-model OD
matrices (low/base/high, beta sensitivity, VGS-calibrated base); 31 benchmark instances (rijnmond_K10/K30/K100_r0–r9 and
rijnmond_strat); baseline results B1–B4 with paired Wilcoxon/Holm statistics; and plausibility/QA reports.
Instance IDs keep the region prefix `rijnmond_` (region identifier used in the paper tables).

## Contents
| path | content |
|---|---|
| `nodes.csv`, `arcs.csv`, `arcs.geojson` | road network |
| `pop_night.tif`, `pop_day.tif`, `cells.npz`, `arc_cells_*.npz` | exposure |
| `gen_points.csv`, `attr_points.csv`, `gateways.csv` | facilities and gateways |
| `od_*.csv`, `gravity_convergence.csv`, `calibration_sites.csv` | OD and calibration |
| `instances/` | benchmark instances |
| `params.yaml`, `DATA_SOURCES.csv`, `erg2024_radii.csv`, `accident_rates_harwood1990.csv` | parameters and provenance |
| `DATA_DICTIONARY.md`, `data_dictionary.csv` | column dictionary |
| `qa_results.json`, `QUALITY_REPORT.txt`, `plausibility_*.csv`, `build_log.txt` | QA |
| `results/` | baselines (K=10, K=30, K=100), stratified baselines, cross-validation, OD sensitivity |
| `light-build/` | total-demand fit, OD sensitivity, calibration cross-validation and the value-of-time sweep, for checking Appendix A, Appendix B and Figure 6. OD matrices of 5 MB or larger are not included. Rebuilding them requires the full pipeline in `code/rotterdamhaz-code-v1.0.1.tgz`. The scripts in `light-build/` cannot generate those matrices |
| `config/` | region config, parameters, source table used for this build |
| `code/rotterdamhaz-code-v1.0.1.tgz` | snapshot of the `hazbench` builder (no virtualenv) |
| `requirements.txt` | pinned Python dependencies (Python 3.13, GDAL 3.12.2) |
| `THIRD_PARTY_DATA.md` | raw inputs not redistributed, with download URLs and licences |
| `LICENSE` | MIT licence for the code; data licences are in `LICENSES.md` |
| `LICENSES.md` | licences per file (ODbL 1.0 / CC BY 4.0 / MIT) and attributions |
| `SHA256SUMS` | checksums; verify with `sha256sum -c SHA256SUMS` |

## How to reproduce
1. Download the raw inputs listed in `THIRD_PARTY_DATA.md` into `data_raw/` (same sub-folder layout).
2. `tar xzf code/rotterdamhaz-code-v1.0.1.tgz && cd code && python3 -m venv .venv && .venv/bin/pip install -r requirements.lock.txt`
3. `export RIJNMOND_ROOT=<project root>; export RIJNMOND_WORK=<work dir>`
4. `scripts/run_region.sh regions/rotterdam.yaml <out_dir>` (prep steps, build, baselines B1–B4, stats, QA; seed 42).
   Build time about 12–14 min on one CPU core for the build + baselines.
5. Assemble with `python -m hazbench.release regions/rotterdam.yaml <out_dir> <release_dir> ...` and compare with `sha256sum -c SHA256SUMS`. A same-seed rebuild reproduces all 54 generated data files byte-for-byte (QA check 9).

## Citation

Cite this dataset archive:

> Liu Q. RotterdamHaz: an open benchmark dataset for hazmat road transport risk. Zenodo. https://doi.org/10.5281/zenodo.23568109

Citation metadata are also provided in `CITATION.cff`. Please cite the accompanying manuscript when referring to the scientific findings. The manuscript title is *A hazardous materials road transport risk dataset for the Rotterdam–Rijnmond port and industrial area*.

## Licence
Network-derived data (network and everything computed on it): ODbL 1.0, © OpenStreetMap contributors. Other data and documentation:
CC BY 4.0. Code: MIT. File-by-file list in `LICENSES.md`.

## Anonymisation
Company and operator names are not included. Facilities carry pseudonymous ids (G01.. generators, A01.. attractors) and a type
(refinery, port terminal, chemical, fuel station, chemical firm). A full rebuild of the facility layer needs the facility list,
which is kept privately by the authors.

## Facility data and intended use
All facility data (locations, site areas, storage and refinery capacities) come only from public sources: operator websites,
OpenStreetMap and the EEA E-PRTR / Industrial Reporting database (plus the public Dutch risk register REV). Facility identifiers are used only to
avoid naming companies, not for confidentiality; capacities and coordinates are given as published. RotterdamHaz is a methodological
benchmark for routing and risk-assessment methods. Its results are not a safety assessment of any specific facility, operator or company.
