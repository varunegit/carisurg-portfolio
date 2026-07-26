# Model Selection — Audit Trail

**Status: DRAFT (interim submission).** Numbers below are the Week 7 six-axis
benchmark, run on the held-out test set (`X_test_fe`, `y_test`), same seed
(42) and split (80/20, stratified) throughout. All models trained on the
213 engineered features (demographics excluded — see `use_demographics:
false` in `config.yaml`).

| Model | Key hyperparameters | Accuracy | Recall ESI 1 | Macro F1 | Train (s) | Infer (ms/pred) | Interpretability |
|---|---|---|---|---|---|---|---|
| Baseline (Logistic Regression) | `max_iter=1000` | 0.672 | 0.188 | 0.480 | 14.59 | 0.004 | High |
| Random Forest (untuned) | `n_estimators=300, class_weight=balanced` | 0.637 | 0.000 | 0.385 | 65.30 | 0.244 | Medium |
| **Random Forest (tuned)** ★ | `n_estimators=200, min_samples_leaf=8, max_features=None, max_depth=None` | 0.608 | **0.312** | 0.475 | 365.03 | 0.071 | Medium |
| **Gradient Boosting** ★ | `max_iter=300, learning_rate=0.1, max_depth=6` | 0.539 | **0.312** | 0.407 | 9.51 | 0.015 | Low |
| Small MLP | `hidden_layer_sizes=(64,32), alpha=1e-3` | 0.636 | 0.188 | 0.462 | 237.81 | 0.005 | Low |

★ = candidate finalists. Random Forest (tuned) hyperparameters come from a
3-fold `RandomizedSearchCV` over 8 candidates, optimising macro-F1.

## Reading this table

- **Dr. Reyes' clinical safety priority (ESI-1 recall):** Random Forest
  (tuned) and Gradient Boosting are tied at 0.312 — both catch roughly a
  third of ESI-1 cases. The untuned Random Forest catches none (0.000),
  and the baseline Logistic Regression and MLP both sit at 0.188 — this is
  the class-imbalance failure mode flagged in Week 6.
- **Martina Griffith's deployment criteria:** with recall tied, training
  time becomes the deciding factor. Gradient Boosting trains in 9.51s vs
  365.03s for the tuned Random Forest (~38x faster) and predicts faster
  per-record too (0.015ms vs 0.071ms). Its cost is interpretability — it
  drops to "Low" (needs SHAP to explain a single prediction), vs "Medium"
  for Random Forest (`feature_importances_` available directly).
- **Open decision for Tuesday's final submission:** with ESI-1 recall tied
  between the two finalists, the tradeoff is now training time/inference
  speed (favours Gradient Boosting) vs interpretability/auditability
  (favours Random Forest tuned). `config.yaml` currently pins
  `random_forest_tuned` as a draft default — confirm with Dr. Reyes and
  Martina Griffith before finalising, and record the reasoning in the
  Week 7 decision journal linked from `HANDOVER.md`.

## Link to full reasoning

Full model-comparison reasoning (feature ablations, demographics-in vs
demographics-out, RandomizedSearchCV search space): Week 7 decision journal
— *[add link once published to the repo]*.
