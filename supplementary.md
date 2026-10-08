---
numbering:
  enumerator: S.%s
  heading: false
---

# Supplementary

:::{figure} static/waveform.svg
:label: fig_waveform
Schematic of the spherical tensor encoding waveform used in this study. Linear tensor encoding acquisitions used a standard pulsed gradient spin echo sequence.
:::

:::{figure} #notebook_fig_brainRois_MhD_lmplots
:label: fig_wholeBrain_ageMhD
Regression lines of the Mahalanobis distance (MhD) as a function of age for each group. The MhD tends to increase with age in most ROIs for AD and FTD, while trends in the small LBD group are inconsistent.
:::

:::{table} ANCOVA results for the log-transformed Mahalanobis distance
:label: table_logMhD_ancovaResults
![](#notebook_table_MhD_ancovaResults_significant)

ANCOVA results comparing the four groups on the log-transformed Mahalanobis distance (MhD) for each ROI, controlling for age and sex. F statistic with its residual degrees of freedom (df_err), partial omega squared ($\omega^2_p$) with the lower bound of its 95% confidence interval, and p-values corrected for multiple comparisons with the Benjamini–Yekutieli false discovery rate procedure (p_adj).
:::

:::{table} ANCOVA assumption violations
:label: table_ancova_violations
![](#notebook_table_ancova_violations)

ROI-metric combinations that did not meet the ANCOVA assumptions (before FDR correction). When homogeneity of regression slopes was violated, we refit the ANCOVA model with the interaction between group and the violating covariate. We visually inspected the cases that violated residual normality and kept them in the analysis. We also kept the case that violated homogeneity of variance, as group sizes were approximately balanced (10 to 14 participants per group).
:::

:::{table} Post-hoc pairwise group comparisons
:label: table_posthocResults_significant
![](#notebook_table_posthocResults_significant)

Exploratory post-hoc pairwise group comparisons for the ROI-metric combinations that survived FDR correction in the ANCOVA, based on age- and sex-adjusted estimated marginal means from the ANCOVA models. t statistic with its residual degrees of freedom (df_err), partial Hedges’ g with its 95% confidence interval, and p-values Holm-corrected within each family of six contrasts. Only contrasts with Holm-corrected p < 0.05 are shown.
:::

:::{figure} #notebook_fig_hippocampus_metrics
:label: fig_hippocampus_metrics

Box plots of the metrics for the whole hippocampus, sampled in the HippUnfold surface space, for each group. Each participant contributes one value: the mean of each metric over the six subfields and both hemispheres, and, for volume, the summed volume of the six subfields in both hemispheres (% of TIV).
:::

:::{figure} #notebook_fig_hippocampus_ageMetrics
:label: fig_hippocampus_ageMetrics

Regression lines of the whole-hippocampus metrics from HippUnfold as a function of age for each group. The metrics follow the expected aging trends, with apparently different trends in participants with dementia.
:::


:::{figure} #notebook_fig_macrometricsSubfield
:label: fig_macrometricsSubfield

Line plots of the HippUnfold surface-based metrics (thickness, curvature and gyrification) across the hippocampal subfields for each group. The solid line represents the mean, and the shaded region denotes the 95% confidence interval of the mean (mean ± 1.96 × standard error), computed over both hemispheres of all participants in each group.
:::