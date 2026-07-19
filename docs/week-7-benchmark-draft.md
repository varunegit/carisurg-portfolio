# Week 7 – Draft Benchmark Table (Interim)

**Author:** Varune | Values from Section 15 of `Week_7_Interim_Deliverable.ipynb`, sorted by macro-F1.

| Model | Accuracy | Recall ESI 1 | Macro F1 | Train (s) | Infer (ms/pred) | Explain |
|---|---|---|---|---|---|---|
| Baseline (LogReg) | 0.672 | 0.188 | 0.480 | 14.59 | 0.004 | High |
| Random Forest (tuned) | 0.608 | 0.312 | 0.475 | 365.03 | 0.071 | Medium |
| Small MLP | 0.636 | 0.188 | 0.462 | 237.81 | 0.005 | Low |
| Gradient Boosting | 0.539 | 0.312 | 0.407 | 9.51 | 0.015 | Low |
| Random Forest (untuned) | 0.637 | 0.000 | 0.385 | 65.30 | 0.244 | Medium |

Best Random Forest hyperparameters (`search.best_params_`): *fill in*

Still to add: SHAP figure from Section 15, saved to `docs/figs/`.
