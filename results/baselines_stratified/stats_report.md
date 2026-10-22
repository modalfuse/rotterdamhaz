# Baseline statistics

OD rows per method: {'B1_min_time': 40, 'B1p_min_pure_time': 40, 'B2_min_length': 40, 'B3_min_TR_sum': 40, 'B4_min_PE_sum': 40}

## Median [Q1, Q3] (IQR)

| metric | B1_min_time | B1p_min_pure_time | B2_min_length | B3_min_TR_sum | B4_min_PE_sum |
|---|---|---|---|---|---|
| T_min | 15.38 [6.129, 22.6] (16.5) | 15.38 [6.129, 22.6] (16.5) | 16.31 [6.129, 23.75] (17.6) | 17.54 [6.129, 25.28] (19.1) | 19.49 [6.934, 28.54] (21.6) |
| L_km | 16.88 [4.306, 23.02] (18.7) | 16.88 [4.306, 23.02] (18.7) | 15.27 [4.306, 22.79] (18.5) | 18.55 [4.306, 28.47] (24.2) | 22.11 [6.518, 32.22] (25.7) |
| TR_sum | 9.362e-05 [1.73e-05, 0.0006555] (0.000638) | 9.362e-05 [1.73e-05, 0.0006555] (0.000638) | 9.35e-05 [1.73e-05, 0.000741] (0.000724) | 8.006e-05 [1.532e-05, 0.0003459] (0.000331) | 9.954e-05 [2.18e-05, 0.0006313] (0.000609) |
| R_union | 9.362e-05 [1.73e-05, 0.0006555] (0.000638) | 9.362e-05 [1.73e-05, 0.0006555] (0.000638) | 9.35e-05 [1.73e-05, 0.000741] (0.000724) | 8.006e-05 [1.532e-05, 0.0003459] (0.000331) | 9.954e-05 [2.18e-05, 0.0006313] (0.000609) |
| PE_sum | 7.411e+04 [1.676e+04, 6.912e+05] (6.74e+05) | 7.411e+04 [1.676e+04, 6.912e+05] (6.74e+05) | 1.217e+05 [1.36e+04, 9.092e+05] (8.96e+05) | 5.418e+04 [1.676e+04, 3.196e+05] (3.03e+05) | 5.007e+04 [1.36e+04, 2.797e+05] (2.66e+05) |
| PE_union | 2.627e+04 [6048, 1.029e+05] (9.68e+04) | 2.627e+04 [6048, 1.029e+05] (9.68e+04) | 2.702e+04 [4654, 1.305e+05] (1.26e+05) | 2.535e+04 [6126, 6.753e+04] (6.14e+04) | 2.441e+04 [4599, 6.669e+04] (6.21e+04) |
| DCR_PE | 2.804 [1.877, 6.698] (4.82) | 2.804 [1.877, 6.698] (4.82) | 3.533 [2.079, 7.623] (5.54) | 3.168 [2.418, 4.355] (1.94) | 2.357 [1.777, 3.814] (2.04) |
| dT | 0 [0, 0] (0) | 0 [0, 0] (0) | 0.008699 [0, 0.09395] (0.094) | 0.08985 [0, 0.1302] (0.13) | 0.003234 [0, 0.2043] (0.204) |
| ARR_TR | 0 [0, 0] (0) | 0 [0, 0] (0) | -0.02545 [-0.7261, 0.5175] (1.24) | 1 [1, 1] (0) | -0.05822 [-0.95, 0] (0.95) |

## Paired Wilcoxon signed-rank (two-sided), Holm-corrected within metric

| metric | a | b | n | non-zero | b<a | b>a | median(b-a) | p | p_Holm |
|---|---|---|---|---|---|---|---|---|---|
| T_min | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| T_min | B1_min_time | B2_min_length | 40 | 24 | 0 | 24 | 0.1597 | 1.81e-05 | 0.000181 |
| T_min | B1_min_time | B3_min_TR_sum | 40 | 24 | 0 | 24 | 1.455 | 1.81e-05 | 0.000181 |
| T_min | B1_min_time | B4_min_PE_sum | 40 | 20 | 0 | 20 | 0.07396 | 8.83e-05 | 0.00053 |
| T_min | B1p_min_pure_time | B2_min_length | 40 | 24 | 0 | 24 | 0.1597 | 1.81e-05 | 0.000181 |
| T_min | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 0 | 24 | 1.455 | 1.81e-05 | 0.000181 |
| T_min | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 0 | 20 | 0.07396 | 8.83e-05 | 0.00053 |
| T_min | B2_min_length | B3_min_TR_sum | 40 | 26 | 11 | 15 | 0 | 0.0384 | 0.153 |
| T_min | B2_min_length | B4_min_PE_sum | 40 | 26 | 14 | 12 | 0 | 0.439 | 1 |
| T_min | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 17 | 11 | 0 | 0.466 | 1 |
| L_km | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| L_km | B1_min_time | B2_min_length | 40 | 24 | 24 | 0 | -0.008228 | 1.8e-05 | 0.000144 |
| L_km | B1_min_time | B3_min_TR_sum | 40 | 24 | 1 | 23 | 0.0348 | 0.000128 | 0.000771 |
| L_km | B1_min_time | B4_min_PE_sum | 40 | 20 | 4 | 16 | 0 | 0.00089 | 0.00356 |
| L_km | B1p_min_pure_time | B2_min_length | 40 | 24 | 24 | 0 | -0.008228 | 1.8e-05 | 0.000144 |
| L_km | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 1 | 23 | 0.0348 | 0.000128 | 0.000771 |
| L_km | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 4 | 16 | 0 | 0.00089 | 0.00356 |
| L_km | B2_min_length | B3_min_TR_sum | 40 | 26 | 0 | 26 | 0.1695 | 8.21e-06 | 8.21e-05 |
| L_km | B2_min_length | B4_min_PE_sum | 40 | 26 | 0 | 26 | 0.07021 | 8.28e-06 | 8.21e-05 |
| L_km | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 15 | 13 | 0 | 0.274 | 0.549 |
| TR_sum | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| TR_sum | B1_min_time | B2_min_length | 40 | 24 | 9 | 15 | 0 | 0.0974 | 0.39 |
| TR_sum | B1_min_time | B3_min_TR_sum | 40 | 24 | 24 | 0 | -6.256e-06 | 1.82e-05 | 0.000146 |
| TR_sum | B1_min_time | B4_min_PE_sum | 40 | 20 | 4 | 16 | 0 | 0.0121 | 0.0725 |
| TR_sum | B1p_min_pure_time | B2_min_length | 40 | 24 | 9 | 15 | 0 | 0.0974 | 0.39 |
| TR_sum | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 24 | 0 | -6.256e-06 | 1.82e-05 | 0.000146 |
| TR_sum | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 4 | 16 | 0 | 0.0121 | 0.0725 |
| TR_sum | B2_min_length | B3_min_TR_sum | 40 | 26 | 26 | 0 | -5.149e-06 | 8.29e-06 | 7.46e-05 |
| TR_sum | B2_min_length | B4_min_PE_sum | 40 | 26 | 12 | 14 | 0 | 0.534 | 1 |
| TR_sum | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 0 | 28 | 1.087e-05 | 3.78e-06 | 3.78e-05 |
| R_union | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| R_union | B1_min_time | B2_min_length | 40 | 24 | 9 | 15 | 0 | 0.0975 | 0.39 |
| R_union | B1_min_time | B3_min_TR_sum | 40 | 24 | 24 | 0 | -6.256e-06 | 1.82e-05 | 0.000146 |
| R_union | B1_min_time | B4_min_PE_sum | 40 | 20 | 4 | 16 | 0 | 0.0121 | 0.0725 |
| R_union | B1p_min_pure_time | B2_min_length | 40 | 24 | 9 | 15 | 0 | 0.0975 | 0.39 |
| R_union | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 24 | 0 | -6.256e-06 | 1.82e-05 | 0.000146 |
| R_union | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 4 | 16 | 0 | 0.0121 | 0.0725 |
| R_union | B2_min_length | B3_min_TR_sum | 40 | 26 | 26 | 0 | -5.149e-06 | 8.29e-06 | 7.46e-05 |
| R_union | B2_min_length | B4_min_PE_sum | 40 | 26 | 12 | 14 | 0 | 0.534 | 1 |
| R_union | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 0 | 28 | 1.087e-05 | 3.79e-06 | 3.79e-05 |
| PE_sum | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| PE_sum | B1_min_time | B2_min_length | 40 | 24 | 2 | 22 | 1307 | 6.32e-05 | 0.000505 |
| PE_sum | B1_min_time | B3_min_TR_sum | 40 | 24 | 7 | 17 | 0 | 0.278 | 0.835 |
| PE_sum | B1_min_time | B4_min_PE_sum | 40 | 20 | 20 | 0 | -5.25 | 8.83e-05 | 0.00053 |
| PE_sum | B1p_min_pure_time | B2_min_length | 40 | 24 | 2 | 22 | 1307 | 6.32e-05 | 0.000505 |
| PE_sum | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 7 | 17 | 0 | 0.278 | 0.835 |
| PE_sum | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 20 | 0 | -5.25 | 8.83e-05 | 0.00053 |
| PE_sum | B2_min_length | B3_min_TR_sum | 40 | 26 | 11 | 15 | 0 | 0.209 | 0.835 |
| PE_sum | B2_min_length | B4_min_PE_sum | 40 | 26 | 26 | 0 | -2667 | 8.26e-06 | 7.43e-05 |
| PE_sum | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 28 | 0 | -7526 | 3.78e-06 | 3.78e-05 |
| PE_union | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| PE_union | B1_min_time | B2_min_length | 40 | 24 | 10 | 14 | 0 | 0.103 | 0.62 |
| PE_union | B1_min_time | B3_min_TR_sum | 40 | 24 | 12 | 12 | 0 | 0.0632 | 0.584 |
| PE_union | B1_min_time | B4_min_PE_sum | 40 | 20 | 12 | 8 | 0 | 0.108 | 0.62 |
| PE_union | B1p_min_pure_time | B2_min_length | 40 | 24 | 10 | 14 | 0 | 0.103 | 0.62 |
| PE_union | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 12 | 12 | 0 | 0.0632 | 0.584 |
| PE_union | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 12 | 8 | 0 | 0.108 | 0.62 |
| PE_union | B2_min_length | B3_min_TR_sum | 40 | 26 | 14 | 12 | 0 | 0.0864 | 0.605 |
| PE_union | B2_min_length | B4_min_PE_sum | 40 | 26 | 16 | 10 | 0 | 0.0584 | 0.584 |
| PE_union | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 15 | 13 | 0 | 0.35 | 0.701 |
| DCR_PE | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| DCR_PE | B1_min_time | B2_min_length | 40 | 24 | 1 | 23 | 0.1976 | 3.02e-05 | 0.000242 |
| DCR_PE | B1_min_time | B3_min_TR_sum | 40 | 24 | 6 | 18 | 0 | 0.253 | 0.759 |
| DCR_PE | B1_min_time | B4_min_PE_sum | 40 | 20 | 15 | 5 | 0 | 0.00422 | 0.0253 |
| DCR_PE | B1p_min_pure_time | B2_min_length | 40 | 24 | 1 | 23 | 0.1976 | 3.02e-05 | 0.000242 |
| DCR_PE | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 6 | 18 | 0 | 0.253 | 0.759 |
| DCR_PE | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 15 | 5 | 0 | 0.00422 | 0.0253 |
| DCR_PE | B2_min_length | B3_min_TR_sum | 40 | 26 | 14 | 12 | 0 | 0.112 | 0.45 |
| DCR_PE | B2_min_length | B4_min_PE_sum | 40 | 26 | 25 | 1 | -0.2412 | 2.1e-05 | 0.000189 |
| DCR_PE | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 27 | 1 | -0.3761 | 1.51e-05 | 0.000151 |
| dT | B1_min_time | B1p_min_pure_time | 40 | 0 | 0 | 0 | 0 | 1 | 1 |
| dT | B1_min_time | B2_min_length | 40 | 24 | 0 | 24 | 0.008699 | 1.81e-05 | 0.000145 |
| dT | B1_min_time | B3_min_TR_sum | 40 | 24 | 0 | 24 | 0.08985 | 1.81e-05 | 0.000145 |
| dT | B1_min_time | B4_min_PE_sum | 40 | 20 | 0 | 20 | 0.003234 | 1.91e-06 | 1.91e-05 |
| dT | B1p_min_pure_time | B2_min_length | 40 | 24 | 0 | 24 | 0.008699 | 1.81e-05 | 0.000145 |
| dT | B1p_min_pure_time | B3_min_TR_sum | 40 | 24 | 0 | 24 | 0.08985 | 1.81e-05 | 0.000145 |
| dT | B1p_min_pure_time | B4_min_PE_sum | 40 | 20 | 0 | 20 | 0.003234 | 1.91e-06 | 1.91e-05 |
| dT | B2_min_length | B3_min_TR_sum | 40 | 26 | 11 | 15 | 0 | 0.0262 | 0.105 |
| dT | B2_min_length | B4_min_PE_sum | 40 | 26 | 14 | 12 | 0 | 0.159 | 0.476 |
| dT | B3_min_TR_sum | B4_min_PE_sum | 40 | 28 | 17 | 11 | 0 | 0.6 | 1 |
| ARR_TR | B1_min_time | B1p_min_pure_time | 24 | 0 | 0 | 0 | 0 | 1 | 1 |
| ARR_TR | B1_min_time | B2_min_length | 24 | 22 | 13 | 9 | -0.02545 | 0.445 | 1 |
| ARR_TR | B1_min_time | B3_min_TR_sum | 24 | 24 | 0 | 24 | 1 | 9.63e-07 | 9.63e-06 |
| ARR_TR | B1_min_time | B4_min_PE_sum | 24 | 16 | 12 | 4 | -0.05822 | 0.0182 | 0.109 |
| ARR_TR | B1p_min_pure_time | B2_min_length | 24 | 22 | 13 | 9 | -0.02545 | 0.445 | 1 |
| ARR_TR | B1p_min_pure_time | B3_min_TR_sum | 24 | 24 | 0 | 24 | 1 | 9.63e-07 | 9.63e-06 |
| ARR_TR | B1p_min_pure_time | B4_min_PE_sum | 24 | 16 | 12 | 4 | -0.05822 | 0.0182 | 0.109 |
| ARR_TR | B2_min_length | B3_min_TR_sum | 24 | 24 | 0 | 24 | 1.025 | 1.82e-05 | 0.000134 |
| ARR_TR | B2_min_length | B4_min_PE_sum | 24 | 23 | 12 | 11 | -0.007527 | 0.465 | 1 |
| ARR_TR | B3_min_TR_sum | B4_min_PE_sum | 24 | 24 | 24 | 0 | -1.058 | 1.68e-05 | 0.000134 |

Share of OD rows where B4 selects the same path as B3: 0.30
