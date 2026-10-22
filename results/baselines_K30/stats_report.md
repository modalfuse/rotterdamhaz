# Baseline statistics

OD rows per method: {'B1_min_time': 300, 'B1p_min_pure_time': 300, 'B2_min_length': 300, 'B3_min_TR_sum': 300, 'B4_min_PE_sum': 300}

## Median [Q1, Q3] (IQR)

| metric | B1_min_time | B1p_min_pure_time | B2_min_length | B3_min_TR_sum | B4_min_PE_sum |
|---|---|---|---|---|---|
| T_min | 10.76 [3.06, 21.13] (18.1) | 10.76 [3.06, 20.82] (17.8) | 11.6 [3.06, 21.9] (18.8) | 11.3 [3.713, 29.56] (25.8) | 11.74 [3.06, 29.2] (26.1) |
| L_km | 10.48 [2.476, 22.9] (20.4) | 10.48 [2.476, 22.67] (20.2) | 10.03 [2.476, 21.21] (18.7) | 10.53 [2.476, 26.17] (23.7) | 10.49 [2.476, 27.77] (25.3) |
| TR_sum | 6.421e-06 [1.982e-06, 1.985e-05] (1.79e-05) | 6.421e-06 [1.982e-06, 1.918e-05] (1.72e-05) | 6.588e-06 [1.982e-06, 2.341e-05] (2.14e-05) | 5.395e-06 [1.458e-06, 1.069e-05] (9.23e-06) | 6.601e-06 [1.645e-06, 1.61e-05] (1.45e-05) |
| R_union | 6.421e-06 [1.982e-06, 1.985e-05] (1.79e-05) | 6.421e-06 [1.982e-06, 1.918e-05] (1.72e-05) | 6.588e-06 [1.982e-06, 2.341e-05] (2.14e-05) | 5.395e-06 [1.458e-06, 1.069e-05] (9.23e-06) | 6.601e-06 [1.645e-06, 1.61e-05] (1.45e-05) |
| PE_sum | 1.204e+04 [2602, 3.586e+04] (3.33e+04) | 1.204e+04 [2602, 3.479e+04] (3.22e+04) | 1.263e+04 [2619, 8.703e+04] (8.44e+04) | 1.092e+04 [2602, 3.84e+04] (3.58e+04) | 8604 [2548, 2.452e+04] (2.2e+04) |
| PE_union | 4536 [1106, 1.278e+04] (1.17e+04) | 4536 [1106, 1.248e+04] (1.14e+04) | 4536 [1142, 1.691e+04] (1.58e+04) | 4426 [1199, 1.114e+04] (9.94e+03) | 4134 [1101, 1.069e+04] (9.59e+03) |
| DCR_PE | 2.19 [1.666, 2.987] (1.32) | 2.211 [1.671, 3.053] (1.38) | 2.95 [1.837, 4.601] (2.76) | 3.017 [1.973, 3.871] (1.9) | 2.161 [1.686, 2.838] (1.15) |
| dT | 0 [0, 0] (0) | 0 [0, 0] (0) | 0 [0, 0.07552] (0.0755) | 0.03545 [0, 0.4052] (0.405) | 2.051e-05 [0, 0.2811] (0.281) |
| ARR_TR | 0 [0, 0] (0) | 0 [0, 0] (0) | -0.0252 [-2.414, 0.03329] (2.45) | 1 [1, 1] (0) | 0.5304 [0, 0.7885] (0.789) |

## Paired Wilcoxon signed-rank (two-sided), Holm-corrected within metric

| metric | a | b | n | non-zero | b<a | b>a | median(b-a) | p | p_Holm |
|---|---|---|---|---|---|---|---|---|---|
| T_min | B1_min_time | B1p_min_pure_time | 300 | 16 | 16 | 0 | 0 | 0.000433 | 0.000866 |
| T_min | B1_min_time | B2_min_length | 300 | 144 | 9 | 135 | 0 | 4.81e-18 | 1.92e-17 |
| T_min | B1_min_time | B3_min_TR_sum | 300 | 173 | 1 | 172 | 0.5808 | 1.21e-29 | 1.09e-28 |
| T_min | B1_min_time | B4_min_PE_sum | 300 | 153 | 2 | 151 | 0.0004517 | 6.08e-26 | 4.26e-25 |
| T_min | B1p_min_pure_time | B2_min_length | 300 | 144 | 0 | 144 | 0 | 2.21e-25 | 1.33e-24 |
| T_min | B1p_min_pure_time | B3_min_TR_sum | 300 | 173 | 0 | 173 | 0.5844 | 3.84e-30 | 3.84e-29 |
| T_min | B1p_min_pure_time | B4_min_PE_sum | 300 | 153 | 0 | 153 | 0.0004517 | 7.38e-27 | 5.9e-26 |
| T_min | B2_min_length | B3_min_TR_sum | 300 | 182 | 37 | 145 | 0 | 6.68e-22 | 3.34e-21 |
| T_min | B2_min_length | B4_min_PE_sum | 300 | 181 | 71 | 110 | 0 | 2.27e-10 | 6.81e-10 |
| T_min | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 87 | 78 | 0 | 0.809 | 0.809 |
| L_km | B1_min_time | B1p_min_pure_time | 300 | 16 | 15 | 1 | 0 | 0.000636 | 0.00127 |
| L_km | B1_min_time | B2_min_length | 300 | 144 | 144 | 0 | 0 | 2.2e-25 | 1.54e-24 |
| L_km | B1_min_time | B3_min_TR_sum | 300 | 173 | 19 | 154 | 0.000527 | 1.01e-22 | 4.03e-22 |
| L_km | B1_min_time | B4_min_PE_sum | 300 | 153 | 20 | 133 | 0 | 1.91e-20 | 5.74e-20 |
| L_km | B1p_min_pure_time | B2_min_length | 300 | 144 | 144 | 0 | 0 | 2.2e-25 | 1.54e-24 |
| L_km | B1p_min_pure_time | B3_min_TR_sum | 300 | 173 | 14 | 159 | 0.007735 | 2.55e-26 | 2.04e-25 |
| L_km | B1p_min_pure_time | B4_min_PE_sum | 300 | 153 | 16 | 137 | 0 | 3.56e-23 | 1.78e-22 |
| L_km | B2_min_length | B3_min_TR_sum | 300 | 182 | 0 | 182 | 0.5696 | 1.28e-31 | 1.28e-30 |
| L_km | B2_min_length | B4_min_PE_sum | 300 | 181 | 0 | 181 | 0.4011 | 1.87e-31 | 1.68e-30 |
| L_km | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 75 | 90 | 0 | 0.0583 | 0.0583 |
| TR_sum | B1_min_time | B1p_min_pure_time | 300 | 16 | 14 | 2 | 0 | 0.0112 | 0.0112 |
| TR_sum | B1_min_time | B2_min_length | 300 | 144 | 43 | 101 | 0 | 1.08e-07 | 4.31e-07 |
| TR_sum | B1_min_time | B3_min_TR_sum | 300 | 167 | 167 | 0 | -5.086e-07 | 3.71e-29 | 3.34e-28 |
| TR_sum | B1_min_time | B4_min_PE_sum | 300 | 148 | 106 | 42 | 0 | 0.000505 | 0.00151 |
| TR_sum | B1p_min_pure_time | B2_min_length | 300 | 144 | 38 | 106 | 0 | 1.02e-09 | 5.08e-09 |
| TR_sum | B1p_min_pure_time | B3_min_TR_sum | 300 | 167 | 167 | 0 | -5.086e-07 | 3.71e-29 | 3.34e-28 |
| TR_sum | B1p_min_pure_time | B4_min_PE_sum | 300 | 148 | 104 | 44 | 0 | 0.00133 | 0.00267 |
| TR_sum | B2_min_length | B3_min_TR_sum | 300 | 177 | 177 | 0 | -5.028e-07 | 8.48e-31 | 8.48e-30 |
| TR_sum | B2_min_length | B4_min_PE_sum | 300 | 177 | 138 | 39 | 0 | 2.56e-12 | 1.54e-11 |
| TR_sum | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 0 | 165 | 1.552e-07 | 7.9e-29 | 5.53e-28 |
| R_union | B1_min_time | B1p_min_pure_time | 300 | 16 | 14 | 2 | 0 | 0.0111 | 0.0111 |
| R_union | B1_min_time | B2_min_length | 300 | 144 | 43 | 101 | 0 | 1.08e-07 | 4.31e-07 |
| R_union | B1_min_time | B3_min_TR_sum | 300 | 167 | 167 | 0 | -5.086e-07 | 3.71e-29 | 3.34e-28 |
| R_union | B1_min_time | B4_min_PE_sum | 300 | 148 | 106 | 42 | 0 | 0.000505 | 0.00151 |
| R_union | B1p_min_pure_time | B2_min_length | 300 | 144 | 38 | 106 | 0 | 1.01e-09 | 5.07e-09 |
| R_union | B1p_min_pure_time | B3_min_TR_sum | 300 | 167 | 167 | 0 | -5.086e-07 | 3.71e-29 | 3.34e-28 |
| R_union | B1p_min_pure_time | B4_min_PE_sum | 300 | 148 | 104 | 44 | 0 | 0.00133 | 0.00267 |
| R_union | B2_min_length | B3_min_TR_sum | 300 | 177 | 177 | 0 | -5.028e-07 | 8.48e-31 | 8.48e-30 |
| R_union | B2_min_length | B4_min_PE_sum | 300 | 177 | 138 | 39 | 0 | 2.56e-12 | 1.54e-11 |
| R_union | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 0 | 165 | 1.552e-07 | 7.89e-29 | 5.52e-28 |
| PE_sum | B1_min_time | B1p_min_pure_time | 300 | 16 | 4 | 12 | 0 | 0.533 | 0.533 |
| PE_sum | B1_min_time | B2_min_length | 300 | 144 | 10 | 134 | 0 | 5.5e-22 | 3.3e-21 |
| PE_sum | B1_min_time | B3_min_TR_sum | 300 | 167 | 48 | 119 | 0 | 1.34e-06 | 4.01e-06 |
| PE_sum | B1_min_time | B4_min_PE_sum | 300 | 148 | 148 | 0 | 0 | 4.88e-26 | 3.9e-25 |
| PE_sum | B1p_min_pure_time | B2_min_length | 300 | 144 | 11 | 133 | 0 | 1.02e-21 | 5.11e-21 |
| PE_sum | B1p_min_pure_time | B3_min_TR_sum | 300 | 167 | 52 | 115 | 0 | 7.66e-06 | 1.53e-05 |
| PE_sum | B1p_min_pure_time | B4_min_PE_sum | 300 | 148 | 148 | 0 | 0 | 4.88e-26 | 3.9e-25 |
| PE_sum | B2_min_length | B3_min_TR_sum | 300 | 177 | 123 | 54 | 0 | 2.75e-13 | 1.1e-12 |
| PE_sum | B2_min_length | B4_min_PE_sum | 300 | 177 | 177 | 0 | -1039 | 8.45e-31 | 8.45e-30 |
| PE_sum | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 165 | 0 | -687.5 | 7.84e-29 | 7.06e-28 |
| PE_union | B1_min_time | B1p_min_pure_time | 300 | 16 | 8 | 8 | 0 | 0.795 | 0.795 |
| PE_union | B1_min_time | B2_min_length | 300 | 142 | 38 | 104 | 0 | 5.8e-13 | 2.32e-12 |
| PE_union | B1_min_time | B3_min_TR_sum | 300 | 161 | 115 | 46 | 0 | 3.02e-14 | 1.81e-13 |
| PE_union | B1_min_time | B4_min_PE_sum | 300 | 143 | 122 | 21 | 0 | 5.62e-19 | 4.5e-18 |
| PE_union | B1p_min_pure_time | B2_min_length | 300 | 142 | 39 | 103 | 0 | 1.96e-13 | 9.78e-13 |
| PE_union | B1p_min_pure_time | B3_min_TR_sum | 300 | 161 | 110 | 51 | 0 | 1.42e-12 | 4.27e-12 |
| PE_union | B1p_min_pure_time | B4_min_PE_sum | 300 | 143 | 120 | 23 | 0 | 2.78e-18 | 1.95e-17 |
| PE_union | B2_min_length | B3_min_TR_sum | 300 | 172 | 125 | 47 | 0 | 2.27e-19 | 2.05e-18 |
| PE_union | B2_min_length | B4_min_PE_sum | 300 | 172 | 137 | 35 | 0 | 2.81e-22 | 2.81e-21 |
| PE_union | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 105 | 60 | 0 | 0.0328 | 0.0657 |
| DCR_PE | B1_min_time | B1p_min_pure_time | 300 | 16 | 2 | 14 | 0 | 0.00763 | 0.0153 |
| DCR_PE | B1_min_time | B2_min_length | 300 | 144 | 8 | 136 | 0 | 3.03e-23 | 2.37e-22 |
| DCR_PE | B1_min_time | B3_min_TR_sum | 300 | 167 | 25 | 142 | 0 | 8.17e-18 | 4.9e-17 |
| DCR_PE | B1_min_time | B4_min_PE_sum | 300 | 148 | 78 | 70 | 0 | 0.0136 | 0.0153 |
| DCR_PE | B1p_min_pure_time | B2_min_length | 300 | 144 | 8 | 136 | 0 | 2.97e-23 | 2.37e-22 |
| DCR_PE | B1p_min_pure_time | B3_min_TR_sum | 300 | 167 | 24 | 143 | 0 | 1.14e-17 | 5.7e-17 |
| DCR_PE | B1p_min_pure_time | B4_min_PE_sum | 300 | 148 | 83 | 65 | 0 | 0.000781 | 0.00234 |
| DCR_PE | B2_min_length | B3_min_TR_sum | 300 | 177 | 108 | 69 | 0 | 6.78e-05 | 0.000271 |
| DCR_PE | B2_min_length | B4_min_PE_sum | 300 | 177 | 155 | 22 | -0.01491 | 2.29e-24 | 2.06e-23 |
| DCR_PE | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 161 | 4 | -0.1424 | 8.66e-27 | 8.66e-26 |
| dT | B1_min_time | B1p_min_pure_time | 300 | 16 | 16 | 0 | 0 | 3.05e-05 | 6.1e-05 |
| dT | B1_min_time | B2_min_length | 300 | 144 | 9 | 135 | 0 | 5.86e-19 | 2.34e-18 |
| dT | B1_min_time | B3_min_TR_sum | 300 | 173 | 1 | 172 | 0.03545 | 1.23e-29 | 1.11e-28 |
| dT | B1_min_time | B4_min_PE_sum | 300 | 153 | 2 | 151 | 2.051e-05 | 3.82e-26 | 2.67e-25 |
| dT | B1p_min_pure_time | B2_min_length | 300 | 144 | 0 | 144 | 0 | 2.22e-25 | 1.33e-24 |
| dT | B1p_min_pure_time | B3_min_TR_sum | 300 | 173 | 0 | 173 | 0.0394 | 3.84e-30 | 3.84e-29 |
| dT | B1p_min_pure_time | B4_min_PE_sum | 300 | 153 | 0 | 153 | 2.374e-05 | 7.38e-27 | 5.9e-26 |
| dT | B2_min_length | B3_min_TR_sum | 300 | 182 | 37 | 145 | 0 | 1.01e-21 | 5.03e-21 |
| dT | B2_min_length | B4_min_PE_sum | 300 | 181 | 71 | 110 | 0 | 1.14e-11 | 3.41e-11 |
| dT | B3_min_TR_sum | B4_min_PE_sum | 300 | 165 | 87 | 78 | 0 | 0.893 | 0.893 |
| ARR_TR | B1_min_time | B1p_min_pure_time | 167 | 16 | 2 | 14 | 0 | 0.00612 | 0.00612 |
| ARR_TR | B1_min_time | B2_min_length | 167 | 130 | 87 | 43 | -0.0252 | 1.04e-08 | 4.15e-08 |
| ARR_TR | B1_min_time | B3_min_TR_sum | 167 | 167 | 0 | 167 | 1 | 3.35e-38 | 3.35e-37 |
| ARR_TR | B1_min_time | B4_min_PE_sum | 167 | 141 | 35 | 106 | 0.5304 | 0.00183 | 0.00548 |
| ARR_TR | B1p_min_pure_time | B2_min_length | 167 | 130 | 92 | 38 | -0.04893 | 3.76e-10 | 1.88e-09 |
| ARR_TR | B1p_min_pure_time | B3_min_TR_sum | 167 | 167 | 0 | 167 | 1 | 2.57e-35 | 2.32e-34 |
| ARR_TR | B1p_min_pure_time | B4_min_PE_sum | 167 | 141 | 37 | 104 | 0.4754 | 0.00301 | 0.00602 |
| ARR_TR | B2_min_length | B3_min_TR_sum | 167 | 163 | 0 | 163 | 1.025 | 1.41e-28 | 1.13e-27 |
| ARR_TR | B2_min_length | B4_min_PE_sum | 167 | 157 | 32 | 125 | 0.7724 | 5.42e-11 | 3.25e-10 |
| ARR_TR | B3_min_TR_sum | B4_min_PE_sum | 167 | 158 | 158 | 0 | -0.4696 | 1.04e-27 | 7.3e-27 |

Share of OD rows where B4 selects the same path as B3: 0.45
