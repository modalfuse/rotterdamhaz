# Baseline statistics

OD rows per method: {'B1_min_time': 100, 'B1p_min_pure_time': 100, 'B2_min_length': 100, 'B3_min_TR_sum': 100, 'B4_min_PE_sum': 100}

## Median [Q1, Q3] (IQR)

| metric | B1_min_time | B1p_min_pure_time | B2_min_length | B3_min_TR_sum | B4_min_PE_sum |
|---|---|---|---|---|---|
| T_min | 13.48 [4.254, 20.74] (16.5) | 13.48 [4.254, 19.88] (15.6) | 14.33 [4.254, 21.53] (17.3) | 17.83 [4.254, 29.31] (25.1) | 19.57 [4.254, 29.46] (25.2) |
| L_km | 13.15 [3.129, 23.5] (20.4) | 13.15 [3.129, 22.78] (19.7) | 13.15 [3.129, 21.99] (18.9) | 15.8 [3.129, 26.32] (23.2) | 19.64 [3.129, 27.75] (24.6) |
| TR_sum | 8.77e-06 [2.665e-06, 2.227e-05] (1.96e-05) | 8.452e-06 [2.665e-06, 2.192e-05] (1.93e-05) | 8.569e-06 [2.729e-06, 3.215e-05] (2.94e-05) | 6.086e-06 [1.889e-06, 1.316e-05] (1.13e-05) | 7.133e-06 [2.158e-06, 1.7e-05] (1.48e-05) |
| R_union | 8.77e-06 [2.665e-06, 2.227e-05] (1.96e-05) | 8.452e-06 [2.665e-06, 2.192e-05] (1.93e-05) | 8.569e-06 [2.729e-06, 3.215e-05] (2.94e-05) | 6.086e-06 [1.889e-06, 1.316e-05] (1.13e-05) | 7.133e-06 [2.158e-06, 1.7e-05] (1.48e-05) |
| PE_sum | 1.613e+04 [4138, 4.739e+04] (4.33e+04) | 1.7e+04 [4138, 4.739e+04] (4.33e+04) | 1.7e+04 [4269, 7.014e+04] (6.59e+04) | 1.7e+04 [3493, 3.728e+04] (3.38e+04) | 9376 [3456, 2.639e+04] (2.29e+04) |
| PE_union | 5778 [1879, 1.32e+04] (1.13e+04) | 5754 [1879, 1.409e+04] (1.22e+04) | 5853 [1823, 1.553e+04] (1.37e+04) | 5744 [1752, 1.184e+04] (1.01e+04) | 5062 [1796, 1.065e+04] (8.86e+03) |
| DCR_PE | 2.246 [1.729, 3.396] (1.67) | 2.28 [1.751, 3.521] (1.77) | 2.997 [2.043, 4.651] (2.61) | 3.105 [2.19, 3.854] (1.66) | 2.306 [1.739, 2.872] (1.13) |
| dT | 0 [0, 0] (0) | 0 [0, 0] (0) | 0 [0, 0.06418] (0.0642) | 0.08985 [0, 0.4182] (0.418) | 0.00125 [0, 0.2867] (0.287) |
| ARR_TR | 0 [0, 0] (0) | 0 [0, 0] (0) | 0 [-1.743, 0.1254] (1.87) | 1 [1, 1] (0) | 0.5445 [0, 0.8134] (0.813) |

## Paired Wilcoxon signed-rank (two-sided), Holm-corrected within metric

| metric | a | b | n | non-zero | b<a | b>a | median(b-a) | p | p_Holm |
|---|---|---|---|---|---|---|---|---|---|
| T_min | B1_min_time | B1p_min_pure_time | 100 | 6 | 6 | 0 | 0 | 0.0312 | 0.0625 |
| T_min | B1_min_time | B2_min_length | 100 | 51 | 4 | 47 | 0 | 1.1e-05 | 4.39e-05 |
| T_min | B1_min_time | B3_min_TR_sum | 100 | 62 | 0 | 62 | 1.136 | 7.53e-12 | 7.53e-11 |
| T_min | B1_min_time | B4_min_PE_sum | 100 | 52 | 0 | 52 | 0.02758 | 3.5e-10 | 2.8e-09 |
| T_min | B1p_min_pure_time | B2_min_length | 100 | 50 | 0 | 50 | 0.0499 | 7.51e-10 | 4.5e-09 |
| T_min | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 0 | 62 | 1.455 | 7.53e-12 | 7.53e-11 |
| T_min | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 0 | 52 | 0.02758 | 3.5e-10 | 2.8e-09 |
| T_min | B2_min_length | B3_min_TR_sum | 100 | 66 | 11 | 55 | 0.9247 | 7.8e-10 | 4.5e-09 |
| T_min | B2_min_length | B4_min_PE_sum | 100 | 65 | 23 | 42 | 0 | 2.68e-05 | 8.04e-05 |
| T_min | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 36 | 25 | 0 | 0.221 | 0.221 |
| L_km | B1_min_time | B1p_min_pure_time | 100 | 6 | 6 | 0 | 0 | 0.0312 | 0.0625 |
| L_km | B1_min_time | B2_min_length | 100 | 51 | 51 | 0 | -0.005383 | 5.1e-10 | 3.57e-09 |
| L_km | B1_min_time | B3_min_TR_sum | 100 | 62 | 8 | 54 | 0.05701 | 3.47e-09 | 1.7e-08 |
| L_km | B1_min_time | B4_min_PE_sum | 100 | 52 | 7 | 45 | 0 | 3.98e-08 | 1.19e-07 |
| L_km | B1p_min_pure_time | B2_min_length | 100 | 50 | 50 | 0 | -0.001269 | 7.48e-10 | 4.49e-09 |
| L_km | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 5 | 57 | 0.05701 | 4.69e-11 | 3.75e-10 |
| L_km | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 5 | 47 | 0 | 3.41e-09 | 1.7e-08 |
| L_km | B2_min_length | B3_min_TR_sum | 100 | 66 | 0 | 66 | 0.6085 | 1.63e-12 | 1.63e-11 |
| L_km | B2_min_length | B4_min_PE_sum | 100 | 65 | 0 | 65 | 0.5696 | 2.39e-12 | 2.16e-11 |
| L_km | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 32 | 29 | 0 | 0.788 | 0.788 |
| TR_sum | B1_min_time | B1p_min_pure_time | 100 | 6 | 6 | 0 | 0 | 0.0312 | 0.0826 |
| TR_sum | B1_min_time | B2_min_length | 100 | 51 | 22 | 29 | 0 | 0.0303 | 0.0826 |
| TR_sum | B1_min_time | B3_min_TR_sum | 100 | 62 | 62 | 0 | -9.994e-07 | 7.55e-12 | 6.79e-11 |
| TR_sum | B1_min_time | B4_min_PE_sum | 100 | 52 | 39 | 13 | 0 | 0.0188 | 0.0752 |
| TR_sum | B1p_min_pure_time | B2_min_length | 100 | 50 | 18 | 32 | 0 | 0.00328 | 0.0164 |
| TR_sum | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 62 | 0 | -9.994e-07 | 7.55e-12 | 6.79e-11 |
| TR_sum | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 38 | 14 | 0 | 0.0275 | 0.0826 |
| TR_sum | B2_min_length | B3_min_TR_sum | 100 | 66 | 66 | 0 | -6.831e-07 | 1.63e-12 | 1.63e-11 |
| TR_sum | B2_min_length | B4_min_PE_sum | 100 | 65 | 49 | 16 | 0 | 1.29e-05 | 7.72e-05 |
| TR_sum | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 0 | 61 | 6.58e-07 | 1.11e-11 | 7.74e-11 |
| R_union | B1_min_time | B1p_min_pure_time | 100 | 6 | 6 | 0 | 0 | 0.0312 | 0.0826 |
| R_union | B1_min_time | B2_min_length | 100 | 51 | 22 | 29 | 0 | 0.0303 | 0.0826 |
| R_union | B1_min_time | B3_min_TR_sum | 100 | 62 | 62 | 0 | -9.994e-07 | 7.55e-12 | 6.79e-11 |
| R_union | B1_min_time | B4_min_PE_sum | 100 | 52 | 39 | 13 | 0 | 0.0188 | 0.0751 |
| R_union | B1p_min_pure_time | B2_min_length | 100 | 50 | 18 | 32 | 0 | 0.00328 | 0.0164 |
| R_union | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 62 | 0 | -9.994e-07 | 7.55e-12 | 6.79e-11 |
| R_union | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 38 | 14 | 0 | 0.0275 | 0.0826 |
| R_union | B2_min_length | B3_min_TR_sum | 100 | 66 | 66 | 0 | -6.831e-07 | 1.64e-12 | 1.64e-11 |
| R_union | B2_min_length | B4_min_PE_sum | 100 | 65 | 49 | 16 | 0 | 1.29e-05 | 7.72e-05 |
| R_union | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 0 | 61 | 6.58e-07 | 1.1e-11 | 7.73e-11 |
| PE_sum | B1_min_time | B1p_min_pure_time | 100 | 6 | 1 | 5 | 0 | 0.438 | 0.518 |
| PE_sum | B1_min_time | B2_min_length | 100 | 51 | 5 | 46 | 0 | 1.67e-07 | 9.99e-07 |
| PE_sum | B1_min_time | B3_min_TR_sum | 100 | 62 | 22 | 40 | 0 | 0.173 | 0.518 |
| PE_sum | B1_min_time | B4_min_PE_sum | 100 | 52 | 52 | 0 | -13.5 | 3.49e-10 | 2.79e-09 |
| PE_sum | B1p_min_pure_time | B2_min_length | 100 | 50 | 6 | 44 | 0 | 4.27e-07 | 2.14e-06 |
| PE_sum | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 22 | 40 | 0 | 0.218 | 0.518 |
| PE_sum | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 52 | 0 | -13.5 | 3.49e-10 | 2.79e-09 |
| PE_sum | B2_min_length | B3_min_TR_sum | 100 | 66 | 42 | 24 | 0 | 0.000142 | 0.000568 |
| PE_sum | B2_min_length | B4_min_PE_sum | 100 | 65 | 65 | 0 | -992.8 | 2.39e-12 | 2.39e-11 |
| PE_sum | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 61 | 0 | -1201 | 1.1e-11 | 9.89e-11 |
| PE_union | B1_min_time | B1p_min_pure_time | 100 | 6 | 2 | 4 | 0 | 1 | 1 |
| PE_union | B1_min_time | B2_min_length | 100 | 50 | 13 | 37 | 0 | 0.000345 | 0.000997 |
| PE_union | B1_min_time | B3_min_TR_sum | 100 | 60 | 39 | 21 | 0 | 3.13e-05 | 0.000188 |
| PE_union | B1_min_time | B4_min_PE_sum | 100 | 51 | 43 | 8 | 0 | 2.71e-08 | 2.44e-07 |
| PE_union | B1p_min_pure_time | B2_min_length | 100 | 49 | 13 | 36 | 0 | 0.000332 | 0.000997 |
| PE_union | B1p_min_pure_time | B3_min_TR_sum | 100 | 60 | 38 | 22 | 0 | 7.8e-05 | 0.00039 |
| PE_union | B1p_min_pure_time | B4_min_PE_sum | 100 | 51 | 43 | 8 | 0 | 2.71e-08 | 2.44e-07 |
| PE_union | B2_min_length | B3_min_TR_sum | 100 | 64 | 42 | 22 | 0 | 2.32e-06 | 1.62e-05 |
| PE_union | B2_min_length | B4_min_PE_sum | 100 | 64 | 53 | 11 | -73.5 | 9.71e-09 | 9.71e-08 |
| PE_union | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 47 | 14 | 0 | 0.000234 | 0.000937 |
| DCR_PE | B1_min_time | B1p_min_pure_time | 100 | 6 | 0 | 6 | 0 | 0.0312 | 0.0938 |
| DCR_PE | B1_min_time | B2_min_length | 100 | 51 | 5 | 46 | 0 | 6.01e-08 | 4.81e-07 |
| DCR_PE | B1_min_time | B3_min_TR_sum | 100 | 62 | 15 | 47 | 0 | 5.79e-05 | 0.000347 |
| DCR_PE | B1_min_time | B4_min_PE_sum | 100 | 52 | 29 | 23 | 0 | 0.14 | 0.14 |
| DCR_PE | B1p_min_pure_time | B2_min_length | 100 | 50 | 6 | 44 | 0 | 1.19e-07 | 8.3e-07 |
| DCR_PE | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 17 | 45 | 0 | 0.000189 | 0.000943 |
| DCR_PE | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 30 | 22 | 0 | 0.0413 | 0.0938 |
| DCR_PE | B2_min_length | B3_min_TR_sum | 100 | 66 | 43 | 23 | 0 | 0.00873 | 0.0349 |
| DCR_PE | B2_min_length | B4_min_PE_sum | 100 | 65 | 56 | 9 | -0.01526 | 1.1e-08 | 9.86e-08 |
| DCR_PE | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 60 | 1 | -0.1677 | 3.6e-11 | 3.6e-10 |
| dT | B1_min_time | B1p_min_pure_time | 100 | 6 | 6 | 0 | 0 | 0.0312 | 0.0625 |
| dT | B1_min_time | B2_min_length | 100 | 51 | 4 | 47 | 0 | 9.24e-06 | 3.7e-05 |
| dT | B1_min_time | B3_min_TR_sum | 100 | 62 | 0 | 62 | 0.08985 | 7.55e-12 | 7.55e-11 |
| dT | B1_min_time | B4_min_PE_sum | 100 | 52 | 0 | 52 | 0.00125 | 3.5e-10 | 2.8e-09 |
| dT | B1p_min_pure_time | B2_min_length | 100 | 50 | 0 | 50 | 0.001934 | 7.51e-10 | 4.51e-09 |
| dT | B1p_min_pure_time | B3_min_TR_sum | 100 | 62 | 0 | 62 | 0.08985 | 7.55e-12 | 7.55e-11 |
| dT | B1p_min_pure_time | B4_min_PE_sum | 100 | 52 | 0 | 52 | 0.00125 | 3.5e-10 | 2.8e-09 |
| dT | B2_min_length | B3_min_TR_sum | 100 | 66 | 11 | 55 | 0.04349 | 2.37e-09 | 1.19e-08 |
| dT | B2_min_length | B4_min_PE_sum | 100 | 65 | 23 | 42 | 0 | 1.37e-05 | 4.1e-05 |
| dT | B3_min_TR_sum | B4_min_PE_sum | 100 | 61 | 36 | 25 | 0 | 0.28 | 0.28 |
| ARR_TR | B1_min_time | B1p_min_pure_time | 62 | 6 | 0 | 6 | 0 | 0.0312 | 0.0312 |
| ARR_TR | B1_min_time | B2_min_length | 62 | 46 | 24 | 22 | 0 | 0.0111 | 0.0221 |
| ARR_TR | B1_min_time | B3_min_TR_sum | 62 | 62 | 0 | 62 | 1 | 3.43e-15 | 3.43e-14 |
| ARR_TR | B1_min_time | B4_min_PE_sum | 62 | 50 | 11 | 39 | 0.5445 | 0.000433 | 0.00217 |
| ARR_TR | B1p_min_pure_time | B2_min_length | 62 | 45 | 27 | 18 | 0 | 0.00327 | 0.00981 |
| ARR_TR | B1p_min_pure_time | B3_min_TR_sum | 62 | 62 | 0 | 62 | 1 | 4.05e-14 | 3.64e-13 |
| ARR_TR | B1p_min_pure_time | B4_min_PE_sum | 62 | 50 | 12 | 38 | 0.5423 | 0.000643 | 0.00257 |
| ARR_TR | B2_min_length | B3_min_TR_sum | 62 | 61 | 0 | 61 | 1 | 9.98e-12 | 7.98e-11 |
| ARR_TR | B2_min_length | B4_min_PE_sum | 62 | 60 | 15 | 45 | 0.7979 | 7.86e-06 | 4.72e-05 |
| ARR_TR | B3_min_TR_sum | B4_min_PE_sum | 62 | 59 | 59 | 0 | -0.4555 | 2.28e-11 | 1.59e-10 |

Share of OD rows where B4 selects the same path as B3: 0.39
