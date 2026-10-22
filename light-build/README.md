# Light build

The result tables in `work/fit_v1.0.0/`, `work/sens_v1.0.0/`, `work/cv_v1.0.0/` and `work/vot_sens/` correspond to the published RotterdamHaz 1.0.0 release.

The no-toll column of Appendix B is `appendix-b/no-toll-calibration_sites.csv`. It comes from the calculation whose fitted total is 934 times 10^4 t/year. It is not `work/vot_sens/run/no_toll/`, and it is not the with-toll calibration table of RotterdamHaz 1.0.0.

Running these scripts requires `hazbench` unpacked from `code/rotterdamhaz-code-v1.0.1.tgz`. This directory does not contain OD matrices of 5 MB or larger. Rebuilding those matrices requires the full pipeline in that archive. The scripts in this directory cannot generate them.
