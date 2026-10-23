# Licences — RotterdamHaz 1.1.0

Decided by Q. Liu (2026-10-21): network-derived data under ODbL 1.0, other data under CC BY 4.0, code under MIT.

## 1. Open Database License (ODbL) 1.0 — OpenStreetMap-derived database
Full text: https://opendatacommons.org/licenses/odbl/1-0/ (database contents: Database Contents License, https://opendatacommons.org/licenses/dbcl/1-0/).
The road network is derived from OpenStreetMap (Geofabrik extract Zuid-Holland, 2026-10-18). Under ODbL these files, and every file computed
on the network, form a Derivative Database and are offered under ODbL 1.0 (share-alike: if you publicly use an adapted version you must offer it under ODbL):

- `nodes.csv`, `arcs.csv`, `arcs.geojson` (network, per-arc attributes, release frequencies, tunnel categories, toll time)
- `arc_cells_ammonia.npz`, `arc_cells_benzene.npz`, `arc_cells_chlorine.npz`, `arc_cells_lpg.npz` (arc–cell exposure sets)
- `gen_points.csv`, `attr_points.csv`, `gateways.csv` (facility / gateway nodes; fuel-station attractors are OSM POIs)
- `od_low.csv`, `od_base.csv`, `od_high.csv`, `od_base_beta1.5.csv`, `od_base_beta2.5.csv`, `od_base_calibrated.csv`, `gravity_convergence.csv`
- `instances/` (all benchmark instances)
- `calibration_sites.csv`, `plausibility_flows.csv`, `plausibility_lengths.csv`, `plausibility_magnitude_basisnet.csv`
- `results/` (baselines, stratified baselines, cross-validation, OD sensitivity)
- `light-build/` csv, npz and tif files computed on the network (fit, sensitivity, cross-validation and value-of-time tables and rasters)

**Attribution (required):** "Contains information from OpenStreetMap, © OpenStreetMap contributors, which is made available under the
Open Database License (ODbL) 1.0 — https://www.openstreetmap.org/copyright".

## 2. Creative Commons Attribution 4.0 International (CC BY 4.0) — all other data and documentation
Full text: https://creativecommons.org/licenses/by/4.0/legalcode

- `pop_night.tif`, `pop_day.tif`, `cells.npz` (100 m population grid; contains CBS data: "Bron: CBS, Kaart van 100 meter bij 100 meter met statistieken 2023")
- `params.yaml`, `DATA_SOURCES.csv`, `erg2024_radii.csv`, `accident_rates_harwood1990.csv`
- `DATA_DICTIONARY.md`, `data_dictionary.csv`, `qa_results.json`, `QUALITY_REPORT.txt`, `build_log.txt`
- `README.md`, `LICENSES.md`, `THIRD_PARTY_DATA.md`, `config/` (region configuration and source table)
- `light-build/README.md` and the text logs under `light-build/`

Suggested attribution: "RotterdamHaz 1.1.0, Q. Liu (2026), CC BY 4.0" plus the source attributions in `THIRD_PARTY_DATA.md`
(CBS and EEA require attribution; Rijkswaterstaat / PDOK inputs are CC0 or public domain).

## 3. MIT License — code
Applies to `code/rotterdamhaz-code-v1.1.0.tgz` (hazbench builder, scripts, tests), `requirements.txt`, `environment.yml`, and the Python scripts under `light-build/`.

```
MIT License

Copyright (c) 2026 Qiang Liu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Anonymisation
Company and operator names are removed from all files (facilities carry pseudonymous ids G01.., A01.. and a type). Coordinates of the
generator nodes are kept because the benchmark needs them.
