# Week 5 Feasibility Memo

## 1. Verdict

The dataset carries a genuine, near-complete triage label (ESI) and clinically sensible vital sign and chief-complaint patterns, but it is a single US health-system extract with an unexplained lack of missing data, and several caveats below must be resolved before any model output reaches a patient.

## 2. Dataset Summary

55,121 ED encounters, 225 features: demographics, vitals, arrival/disposition, 200 binary chief-complaint flags.

**Target Label — ESI**

| ESI | Encounters | Percentage |
|---|---|---|
| 1 (Resuscitation) | 77 | 0.1% |
| 2 (Emergent) | 17,924 | 32.5% |
| 3 (Urgent) | 27,010 | 49.0% |
| 4 (Less urgent) | 8,896 | 16.1% |
| 5 (Non-urgent) | 1,214 | 2.2% |

Most patients are in the mid-acuity range (ESI 2–3), which makes up 81% of the ESI. ESI 1 is rare, which is a constraint for modelling.

Temperature is recorded in Fahrenheit, not Celsius. This makes it easy to miss for anyone applying standard clinical thresholds.

## 3. Top 3 Concerns

- Zero missing values across all 25 columns
- Outcome leakage risk in two columns
- Extreme sparsity in chief-complaint flags

## 4. Top 3 Reasons to Proceed

- A real, non-synthetic triage label
- Vitals separate acuity in the expected clinical direction
- Chief complaints track acuity sensibly

## 5. Caveats

- Single-country, single-vendor extract
- The vital/complaint relationships do not constitute proof that the model will perform well
- The completeness of this extract, with zero-missingness in a clinical dataset of this size, is atypical
- Severe class imbalance — for example, ESI 1 is 0.1%
