# Decision: Week 7 model choice for ESI triage prediction

**Date:** 21 July 2026
**Author:** Varune

## Context
- The Week 6 logistic regression baseline caught fewer than one in five truly critical (ESI 1) patients.
- A defensible recommendation on whether a more complex model justifies its extra training and inference cost, not simply "the best model."

## Alternatives considered
- **Tuned Random Forest** — matched Gradient Boosting on ESI-1 recall (0.312) and had somewhat better interpretability (Medium vs. Low), but took over 38x longer to train (365.03s vs. 9.51s) for no accuracy or safety gain.
- **Small MLP** — no improvement over the baseline on ESI-1 recall (0.188 vs. 0.188), while costing far more to train (237.81s) and being harder to explain.
- **Gradient Boosting** — matched the tuned Random Forest's ESI-1 recall at a fraction of the training cost, with the lowest overall accuracy and interpretability of the models tested.

## Decision
Recommend Gradient Boosting as the Phase 3 candidate model, conditional on adding a SHAP-based explanation panel before any deployment consideration.

## Reasoning
- Training time is a one-off cost; inference time is paid on every patient indefinitely. Gradient Boosting wins on the cost that actually recurs (0.015 ms/pred) while tying the tuned Random Forest on the metric that matters clinically (ESI-1 recall).
- The interpretability gap (Low vs. Medium) is real but addressable with tooling (SHAP), whereas the training-time gap between Gradient Boosting and the tuned Random Forest is a structural property of the algorithms, not something tuning can close.
- Aggregate accuracy and macro-F1 are lower for Gradient Boosting than for the baseline or tuned Random Forest, optimising for them over ESI-1 recall would repeat the exact trap Week 6 exposed.

## Things I do not yet know
- Whether Gradient Boosting's errors cluster disproportionately in a specific patient subgroup (e.g. those with near-normal vitals) — the stratified error analysis has limited sample size per subgroup and needs revisiting with more data or bootstrapped confidence intervals.
- How stable the 0.312 ESI-1 recall figure is across different train/test splits, since all current results come from a single split with a very small number of ESI 1 encounters in the test set.
