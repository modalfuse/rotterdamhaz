# Baseline statistics

OD rows per method: {'B1_min_time': 1000, 'B1p_min_pure_time': 1000, 'B2_min_length': 1000, 'B3_min_TR_sum': 1000, 'B4_min_PE_sum': 1000}

## Median [Q1, Q3] (IQR)

| metric | B1_min_time | B1p_min_pure_time | B2_min_length | B3_min_TR_sum | B4_min_PE_sum |
|---|---|---|---|---|---|
| T_min | 12.24 [3.102, 21.63] (18.5) | 12.18 [3.102, 20.93] (17.8) | 12.51 [3.102, 22.82] (19.7) | 14.45 [3.171, 30.91] (27.7) | 14.54 [3.102, 27.59] (24.5) |
| L_km | 11.06 [2.419, 22.59] (20.2) | 11.06 [2.419, 22.14] (19.7) | 10.96 [2.419, 20.54] (18.1) | 13 [2.476, 26.67] (24.2) | 14.34 [2.46, 27.36] (24.9) |
| TR_sum | 6.837e-06 [1.982e-06, 1.724e-05] (1.53e-05) | 6.775e-06 [1.982e-06, 1.626e-05] (1.43e-05) | 7.453e-06 [1.982e-06, 2.16e-05] (1.96e-05) | 5.543e-06 [1.421e-06, 1.068e-05] (9.26e-06) | 6.402e-06 [1.684e-06, 1.447e-05] (1.28e-05) |
| R_union | 6.837e-06 [1.982e-06, 1.724e-05] (1.53e-05) | 6.775e-06 [1.982e-06, 1.626e-05] (1.43e-05) | 7.453e-06 [1.982e-06, 2.16e-05] (1.96e-05) | 5.543e-06 [1.421e-06, 1.068e-05] (9.26e-06) | 6.402e-06 [1.684e-06, 1.447e-05] (1.28e-05) |
| PE_sum | 1.443e+04 [3034, 4.2e+04] (3.9e+04) | 1.354e+04 [3034, 4.153e+04] (3.85e+04) | 1.539e+04 [3037, 1.013e+05] (9.82e+04) | 1.329e+04 [3025, 3.954e+04] (3.65e+04) | 9486 [2825, 2.734e+04] (2.45e+04) |
| PE_union | 4634 [1282, 1.414e+04] (1.29e+04) | 4634 [1282, 1.286e+04] (1.16e+04) | 4744 [1296, 1.984e+04] (1.85e+04) | 4271 [1198, 1.104e+04] (9.84e+03) | 4248 [1180, 1.063e+04] (9.45e+03) |
| DCR_PE | 2.576 [1.893, 3.507] (1.61) | 2.584 [1.896, 3.524] (1.63) | 3.488 [2.391, 4.842] (2.45) | 3.154 [2.268, 4.041] (1.77) | 2.269 [1.823, 3.037] (1.21) |
| dT | 0 [0, 0] (0) | 0 [0, 0] (0) | 0 [0, 0.0776] (0.0776) | 0.08568 [0, 0.4438] (0.444) | 0.003718 [0, 0.2676] (0.268) |
| ARR_TR | 0 [0, 0] (0) | 0 [0, 0] (0) | -0.1319 [-2.695, 0] (2.7) | 1 [1, 1] (0) | 0.3263 [0, 0.7702] (0.77) |

## Paired Wilcoxon signed-rank (two-sided), Holm-corrected within metric

| metric | a | b | n | non-zero | b<a | b>a | median(b-a) | p | p_Holm |
|---|---|---|---|---|---|---|---|---|---|
| T_min | B1_min_time | B1p_min_pure_time | 1000 | 50 | 50 | 0 | 0 | 7.28e-10 | 1.46e-09 |
| T_min | B1_min_time | B2_min_length | 1000 | 502 | 28 | 474 | 0 | 2.34e-65 | 9.35e-65 |
| T_min | B1_min_time | B3_min_TR_sum | 1000 | 640 | 8 | 632 | 0.8448 | 1.36e-103 | 1.22e-102 |
| T_min | B1_min_time | B4_min_PE_sum | 1000 | 559 | 18 | 541 | 0.08079 | 2.61e-84 | 1.83e-83 |
| T_min | B1p_min_pure_time | B2_min_length | 1000 | 500 | 0 | 500 | 0.02548 | 1.24e-83 | 7.44e-83 |
| T_min | B1p_min_pure_time | B3_min_TR_sum | 1000 | 640 | 0 | 640 | 1.061 | 1.77e-106 | 1.77e-105 |
| T_min | B1p_min_pure_time | B4_min_PE_sum | 1000 | 557 | 0 | 557 | 0.1256 | 6.23e-93 | 4.99e-92 |
| T_min | B2_min_length | B3_min_TR_sum | 1000 | 655 | 134 | 521 | 0.145 | 1.44e-70 | 7.21e-70 |
| T_min | B2_min_length | B4_min_PE_sum | 1000 | 638 | 256 | 382 | 0 | 6.45e-26 | 1.93e-25 |
| T_min | B3_min_TR_sum | B4_min_PE_sum | 1000 | 630 | 377 | 253 | 0 | 5.71e-05 | 5.71e-05 |
| L_km | B1_min_time | B1p_min_pure_time | 1000 | 50 | 48 | 2 | 0 | 9.24e-09 | 1.85e-08 |
| L_km | B1_min_time | B2_min_length | 1000 | 502 | 502 | 0 | -0.002538 | 5.61e-84 | 3.37e-83 |
| L_km | B1_min_time | B3_min_TR_sum | 1000 | 640 | 78 | 562 | 0.1456 | 1.68e-84 | 1.18e-83 |
| L_km | B1_min_time | B4_min_PE_sum | 1000 | 559 | 77 | 482 | 0 | 2.3e-68 | 6.91e-68 |
| L_km | B1p_min_pure_time | B2_min_length | 1000 | 500 | 500 | 0 | -0.001269 | 1.19e-83 | 5.95e-83 |
| L_km | B1p_min_pure_time | B3_min_TR_sum | 1000 | 640 | 60 | 580 | 0.4108 | 4.84e-95 | 3.87e-94 |
| L_km | B1p_min_pure_time | B4_min_PE_sum | 1000 | 557 | 59 | 498 | 0 | 6.15e-79 | 2.46e-78 |
| L_km | B2_min_length | B3_min_TR_sum | 1000 | 655 | 0 | 655 | 1.164 | 6.3e-109 | 6.3e-108 |
| L_km | B2_min_length | B4_min_PE_sum | 1000 | 638 | 0 | 638 | 0.9782 | 3.73e-106 | 3.36e-105 |
| L_km | B3_min_TR_sum | B4_min_PE_sum | 1000 | 630 | 322 | 308 | 0 | 0.585 | 0.585 |
| TR_sum | B1_min_time | B1p_min_pure_time | 1000 | 50 | 45 | 5 | 0 | 1.85e-08 | 1.85e-08 |
| TR_sum | B1_min_time | B2_min_length | 1000 | 502 | 126 | 376 | 0 | 1.8e-38 | 7.21e-38 |
| TR_sum | B1_min_time | B3_min_TR_sum | 1000 | 624 | 624 | 0 | -6.831e-07 | 7.22e-104 | 5.78e-103 |
| TR_sum | B1_min_time | B4_min_PE_sum | 1000 | 546 | 369 | 177 | 0 | 2.71e-14 | 8.14e-14 |
| TR_sum | B1p_min_pure_time | B2_min_length | 1000 | 500 | 95 | 405 | 0 | 7.35e-51 | 4.41e-50 |
| TR_sum | B1p_min_pure_time | B3_min_TR_sum | 1000 | 624 | 624 | 0 | -6.591e-07 | 7.22e-104 | 5.78e-103 |
| TR_sum | B1p_min_pure_time | B4_min_PE_sum | 1000 | 544 | 350 | 194 | 0 | 1.2e-09 | 2.41e-09 |
| TR_sum | B2_min_length | B3_min_TR_sum | 1000 | 648 | 648 | 0 | -1.081e-06 | 8.75e-108 | 8.75e-107 |
| TR_sum | B2_min_length | B4_min_PE_sum | 1000 | 634 | 500 | 134 | -2.27e-10 | 1.05e-46 | 5.24e-46 |
| TR_sum | B3_min_TR_sum | B4_min_PE_sum | 1000 | 630 | 0 | 630 | 4.663e-07 | 7.58e-105 | 6.82e-104 |
| R_union | B1_min_time | B1p_min_pure_time | 1000 | 50 | 45 | 5 | 0 | 1.84e-08 | 1.84e-08 |
| R_union | B1_min_time | B2_min_length | 1000 | 502 | 126 | 376 | 0 | 1.79e-38 | 7.18e-38 |
| R_union | B1_min_time | B3_min_TR_sum | 1000 | 624 | 624 | 0 | -6.831e-07 | 7.22e-104 | 5.78e-103 |
| R_union | B1_min_time | B4_min_PE_sum | 1000 | 546 | 369 | 177 | 0 | 2.71e-14 | 8.14e-14 |
| R_union | B1p_min_pure_time | B2_min_length | 1000 | 500 | 95 | 405 | 0 | 7.31e-51 | 4.38e-50 |
| R_union | B1p_min_pure_time | B3_min_TR_sum | 1000 | 624 | 624 | 0 | -6.591e-07 | 7.22e-104 | 5.78e-103 |
| R_union | B1p_min_pure_time | B4_min_PE_sum | 1000 | 544 | 350 | 194 | 0 | 1.2e-09 | 2.41e-09 |
| R_union | B2_min_length | B3_min_TR_sum | 1000 | 648 | 648 | 0 | -1.081e-06 | 8.75e-108 | 8.75e-107 |
| R_union | B2_min_length | B4_min_PE_sum | 1000 | 634 | 500 | 134 | -2.27e-10 | 1.05e-46 | 5.24e-46 |
| R_union | B3_min_TR_sum | B4_min_PE_sum | 1000 | 630 | 0 | 630 | 4.663e-07 | 7.57e-105 | 6.82e-104 |
| PE_sum | B1_min_time | B1p_min_pure_time | 1000 | 50 | 38 | 12 | 0 | 3.92e-07 | 1.18e-06 |
| PE_sum | B1_min_time | B2_min_length | 1000 | 502 | 67 | 435 | 0 | 4.55e-58 | 2.27e-57 |
| PE_sum | B1_min_time | B3_min_TR_sum | 1000 | 621 | 249 | 372 | 0 | 0.0014 | 0.0014 |
| PE_sum | B1_min_time | B4_min_PE_sum | 1000 | 546 | 546 | 0 | -135 | 3.87e-91 | 3.1e-90 |
| PE_sum | B1p_min_pure_time | B2_min_length | 1000 | 500 | 56 | 444 | 0 | 1.23e-62 | 7.4e-62 |
| PE_sum | B1p_min_pure_time | B3_min_TR_sum | 1000 | 621 | 245 | 376 | 0 | 0.000105 | 0.00021 |
| PE_sum | B1p_min_pure_time | B4_min_PE_sum | 1000 | 544 | 544 | 0 | -135 | 8.21e-91 | 5.75e-90 |
| PE_sum | B2_min_length | B3_min_TR_sum | 1000 | 646 | 465 | 181 | 0 | 9.26e-52 | 3.7e-51 |
| PE_sum | B2_min_length | B4_min_PE_sum | 1000 | 634 | 634 | 0 | -1640 | 1.67e-105 | 1.67e-104 |
| PE_sum | B3_min_TR_sum | B4_min_PE_sum | 1000 | 629 | 629 | 0 | -874 | 1.09e-104 | 9.83e-104 |
| PE_union | B1_min_time | B1p_min_pure_time | 1000 | 50 | 38 | 12 | 0 | 1.39e-07 | 2.77e-07 |
| PE_union | B1_min_time | B2_min_length | 1000 | 493 | 161 | 332 | 0 | 2.62e-33 | 7.87e-33 |
| PE_union | B1_min_time | B3_min_TR_sum | 1000 | 596 | 448 | 148 | 0 | 3.32e-59 | 1.99e-58 |
| PE_union | B1_min_time | B4_min_PE_sum | 1000 | 539 | 462 | 77 | 0 | 1.63e-67 | 1.46e-66 |
| PE_union | B1p_min_pure_time | B2_min_length | 1000 | 492 | 144 | 348 | 0 | 3.02e-41 | 1.21e-40 |
| PE_union | B1p_min_pure_time | B3_min_TR_sum | 1000 | 596 | 427 | 169 | 0 | 1.06e-50 | 5.3e-50 |
| PE_union | B1p_min_pure_time | B4_min_PE_sum | 1000 | 537 | 453 | 84 | 0 | 1.06e-64 | 7.41e-64 |
| PE_union | B2_min_length | B3_min_TR_sum | 1000 | 628 | 467 | 161 | 0 | 3.86e-65 | 3.09e-64 |
| PE_union | B2_min_length | B4_min_PE_sum | 1000 | 623 | 493 | 130 | 0 | 5.49e-77 | 5.49e-76 |
| PE_union | B3_min_TR_sum | B4_min_PE_sum | 1000 | 620 | 363 | 257 | 0 | 0.008 | 0.008 |
| DCR_PE | B1_min_time | B1p_min_pure_time | 1000 | 50 | 9 | 41 | 0 | 0.000278 | 0.000278 |
| DCR_PE | B1_min_time | B2_min_length | 1000 | 502 | 39 | 463 | 0 | 6.31e-76 | 5.05e-75 |
| DCR_PE | B1_min_time | B3_min_TR_sum | 1000 | 623 | 144 | 479 | 0 | 4.83e-38 | 2.9e-37 |
| DCR_PE | B1_min_time | B4_min_PE_sum | 1000 | 546 | 357 | 189 | 0 | 4.62e-26 | 1.39e-25 |
| DCR_PE | B1p_min_pure_time | B2_min_length | 1000 | 500 | 42 | 458 | 0 | 3.58e-74 | 2.5e-73 |
| DCR_PE | B1p_min_pure_time | B3_min_TR_sum | 1000 | 623 | 148 | 475 | 0 | 1.81e-36 | 9.07e-36 |
| DCR_PE | B1p_min_pure_time | B4_min_PE_sum | 1000 | 544 | 367 | 177 | 0 | 3.09e-29 | 1.24e-28 |
| DCR_PE | B2_min_length | B3_min_TR_sum | 1000 | 646 | 428 | 218 | 0 | 2.76e-22 | 5.51e-22 |
| DCR_PE | B2_min_length | B4_min_PE_sum | 1000 | 634 | 596 | 38 | -0.3659 | 2.7e-95 | 2.7e-94 |
| DCR_PE | B3_min_TR_sum | B4_min_PE_sum | 1000 | 629 | 607 | 22 | -0.2767 | 3.75e-94 | 3.37e-93 |
| dT | B1_min_time | B1p_min_pure_time | 1000 | 50 | 50 | 0 | 0 | 7.54e-10 | 1.51e-09 |
| dT | B1_min_time | B2_min_length | 1000 | 502 | 28 | 474 | 0 | 1.15e-67 | 4.58e-67 |
| dT | B1_min_time | B3_min_TR_sum | 1000 | 640 | 8 | 632 | 0.08568 | 2.35e-104 | 2.12e-103 |
| dT | B1_min_time | B4_min_PE_sum | 1000 | 559 | 18 | 541 | 0.003718 | 3.82e-86 | 2.67e-85 |
| dT | B1p_min_pure_time | B2_min_length | 1000 | 500 | 0 | 500 | 0.0009185 | 1.26e-83 | 7.58e-83 |
| dT | B1p_min_pure_time | B3_min_TR_sum | 1000 | 640 | 0 | 640 | 0.0996 | 1.77e-106 | 1.77e-105 |
| dT | B1p_min_pure_time | B4_min_PE_sum | 1000 | 557 | 0 | 557 | 0.006291 | 6.24e-93 | 4.99e-92 |
| dT | B2_min_length | B3_min_TR_sum | 1000 | 655 | 134 | 521 | 0.01257 | 2.22e-73 | 1.11e-72 |
| dT | B2_min_length | B4_min_PE_sum | 1000 | 638 | 256 | 382 | 0 | 1.64e-30 | 4.93e-30 |
| dT | B3_min_TR_sum | B4_min_PE_sum | 1000 | 630 | 377 | 253 | 0 | 0.00131 | 0.00131 |
| ARR_TR | B1_min_time | B1p_min_pure_time | 624 | 50 | 5 | 45 | 0 | 9.62e-07 | 2.89e-06 |
| ARR_TR | B1_min_time | B2_min_length | 624 | 463 | 337 | 126 | -0.1319 | 9.93e-42 | 4.97e-41 |
| ARR_TR | B1_min_time | B3_min_TR_sum | 624 | 624 | 0 | 624 | 1 | 1.01e-137 | 1.01e-136 |
| ARR_TR | B1_min_time | B4_min_PE_sum | 624 | 521 | 152 | 369 | 0.3263 | 1.93e-06 | 3.87e-06 |
| ARR_TR | B1p_min_pure_time | B2_min_length | 624 | 461 | 366 | 95 | -0.1966 | 1.02e-49 | 6.12e-49 |
| ARR_TR | B1p_min_pure_time | B3_min_TR_sum | 624 | 624 | 0 | 624 | 1 | 2.06e-128 | 1.85e-127 |
| ARR_TR | B1p_min_pure_time | B4_min_PE_sum | 624 | 519 | 169 | 350 | 0.2125 | 8.81e-05 | 8.81e-05 |
| ARR_TR | B2_min_length | B3_min_TR_sum | 624 | 609 | 0 | 609 | 1.132 | 7.02e-102 | 5.62e-101 |
| ARR_TR | B2_min_length | B4_min_PE_sum | 624 | 575 | 113 | 462 | 0.8948 | 3.97e-38 | 1.59e-37 |
| ARR_TR | B3_min_TR_sum | B4_min_PE_sum | 624 | 605 | 605 | 0 | -0.6737 | 6.94e-101 | 4.86e-100 |

Share of OD rows where B4 selects the same path as B3: 0.37
