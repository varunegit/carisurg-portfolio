# Model Selection — Audit Trail

Six-axis benchmark, run on the held-out test set (`X_test_fe`, `y_test`),
seed 42, 80/20 stratified split, throughout. All models trained on the
engineered feature set (demographics excluded — see `use_demographics:
false` in `config.yaml`).

| Model | Accuracy | Precision (macro) | Recall (macro) | Recall ESI 1 | Macro F1 | Train (s) | Infer (ms/pred) | Interpretability |
|---|---|---|---|---|---|---|---|---|
| Baseline (Logistic Regression) | 0.670 | 0.569 | 0.464 | 0.250 | 0.490 | 8.09 | 0.003 | High |
| Baseline (Decision Tree) | 0.563 | 0.389 | 0.383 | 0.062 | 0.386 | 3.76 | 0.003 | High |
| Random Forest (untuned) | 0.649 | 0.575 | 0.395 | 0.062 | 0.426 | 69.98 | 0.150 | Medium |
| Random Forest (tuned) | 0.607 | 0.453 | 0.523 | 0.312 | 0.476 | 350.12 | 0.073 | Medium |
| **Gradient Boosting (recommended)** | 0.561 | 0.425 | **0.581** | **0.438** | 0.437 | **14.83** | 0.025 | Low |
| Small MLP | 0.638 | 0.443 | 0.418 | 0.062 | 0.426 | 412.63 | 0.016 | Low |

Random Forest (tuned) hyperparameters come from a 3-fold
`RandomizedSearchCV` over 8 candidates, optimising macro-F1.

## Reading this table

- **Dr. Reyes' clinical safety priority (ESI-1 recall):** Gradient
  Boosting leads clearly at 0.438, well ahead of the tuned Random Forest
  (0.312). It also has the best macro-recall of any model (0.581),
  meaning it catches more true positives across all five ESI levels, not
  just level 1. The untuned Random Forest, Decision Tree baseline, and
  MLP all sit at 0.062 ESI-1 recall — the class-imbalance failure mode
  flagged in Week 6.
- **Martina Griffith's deployment criteria:** Gradient Boosting trains in
  14.83s vs 350.12s for the tuned Random Forest (~24x faster) and predicts
  in 0.025ms vs 0.073ms per record. Its cost is interpretability — "Low"
  (requires SHAP to explain a single prediction) vs "Medium" for Random
  Forest (`feature_importances_` available directly).
- **Precision (macro) is lower for Gradient Boosting (0.425) than for the
  baseline (0.569) or the untuned Random Forest (0.575).** This means
  Gradient Boosting flags more false positives across the five ESI levels
  in exchange for catching more true positives — a reasonable trade for a
  triage safety-net model, but worth naming explicitly rather than only
  reporting the recall gain.

## Final decision

**Gradient Boosting** — full reasoning in
`docs/decisions/2026-week-7-model-choice.md`, conditional on adding a
SHAP-based explanation panel before deployment.
