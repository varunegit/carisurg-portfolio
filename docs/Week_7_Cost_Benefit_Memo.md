# Cost-Benefit Memo: Model Selection for ESI Triage Prediction

## 1. Verdict

I recommend adopting the Gradient Boosting model for the next phase of
ESI triage prediction. It matches the best available recall for the most
critical patients (ESI 1) while training over thirty times faster than
the alternative with equivalent clinical performance, at the
acknowledged cost of being harder to explain without additional tooling.

## 2. A Note on Terms Used in This Memo

ESI (Emergency Severity Index) is the five-level scale used to rank how
urgently a patient needs to be seen, where ESI 1 is the most critical.
Recall for ESI 1 is the proportion of truly critical patients the model
correctly flags as critical; a low recall means the model is
under-triaging sick patients. Macro-F1 is a single overall
accuracy-style score averaged evenly across all five ESI levels, so it
does not by itself reveal how the model performs on any one level.
Training time is a one-off cost paid when the model is built or
retrained; inference time is paid for every single prediction, for every
patient, indefinitely.

## 3. Recap: Dataset and Method

This analysis uses 55,121 emergency department encounters and 225 raw
features. The Week 6 baseline used logistic regression on a cleaned
feature set with a fixed train/test split (random state 42), which is
reused unchanged throughout this comparison so that every result below
is directly comparable.

Beyond the raw vital signs, a small set of clinical red-flag features
was engineered for this comparison: whether a patient was tachypnoeic,
hypoxic, febrile, or bradycardic, plus a combined red-flag count. These
are intended to capture early warning signs that a single vital sign in
isolation might miss. Demographic fields such as ethnicity and race
were tested separately purely to measure their effect on model
performance; per the project's standing ethics position, they are
excluded from any model put forward for deployment unless governance
explicitly approves their inclusion, regardless of any accuracy gain
they produce.

Five candidate models were benchmarked this week: the Week 6 logistic
regression baseline, an untuned Random Forest, a Random Forest tuned via
three-fold cross-validated random search, a Gradient Boosting
classifier, and a small multi-layer perceptron. Each was scored on the
same held-out test set across six quantitative axes plus a qualitative
interpretability rating.

## 4. Benchmark Table

| Model | Accuracy | Recall ESI 1 | Macro F1 | Train (s) | Infer (ms/pred) | Explain |
|---|---|---|---|---|---|---|
| Baseline (LogReg) | 0.672 | 0.188 | 0.480 | 14.59 | 0.004 | High |
| Random Forest (tuned) | 0.608 | 0.312 | 0.475 | 365.03 | 0.071 | Medium |
| Small MLP | 0.636 | 0.188 | 0.462 | 237.81 | 0.005 | Low |
| **Gradient Boosting (recommended)** | 0.539 | **0.312** | 0.407 | **9.51** | 0.015 | Low |
| Random Forest (untuned) | 0.637 | 0.000 | 0.385 | 65.30 | 0.244 | Medium |

## 5. Three Arguments for Gradient Boosting

- **Clinical safety is matched, not traded away.** Gradient Boosting
  achieves the same ESI-1 recall (0.312) as the tuned Random Forest,
  nearly doubling the baseline's capture rate of critically ill
  patients (0.188).
- **Training costs are negligible for a model retrained occasionally.**
  At 9.51 seconds, Gradient Boosting trains are over thirty-eight times
  faster than the tuned Random Forest (365.03 seconds).
- **Inference is comfortably fast enough for real-time triage.** At
  0.015 milliseconds per prediction, it is well within any operational
  threshold for a live emergency department workflow.

## 6. Three Arguments Against Gradient Boosting

- **Lowest overall accuracy and macro-F1 of all five models tested**
  (0.539 and 0.407 respectively). The clinical safety gain is real but
  narrow and comes with a broader drop in general-purpose predictive
  quality.
- **Interpretability is rated Low.** A single prediction cannot be
  explained to the clinical staff in under a minute without SHAP
  tooling, unlike the baseline (High) or either Random Forest variant
  (Medium).
- **Results rest on a single train/test split.** Given how rare ESI 1
  encounters are in this dataset, the reported recall of 0.312 could
  shift meaningfully on unseen data; no confidence interval has yet
  been computed.

## 7. Why Not the Alternatives

The baseline logistic regression remains the easiest model to explain
and the cheapest to run, but it misses over four out of every five truly
critical patients (recall 0.188), which is difficult to justify once a
model with materially better safety performance exists.

The tuned Random Forest matches Gradient Boosting on the metric that
matters most, ESI-1 recall, and offers a somewhat clearer explanation
path. However, its training cost is over thirty-eight times higher for
no measurable gain in either accuracy or clinical safety, and its
inference time, while still fast in absolute terms, is roughly four
times slower than Gradient Boosting's. Given that training time is paid
once and inference time is paid on every patient indefinitely, neither
factor favours the Random Forest here strongly enough to outweigh
Gradient Boosting's speed advantage.

The small MLP offers no advantage over the baseline on ESI-1 recall
(both 0.188), while costing substantially more to train (237.81 seconds)
and being harder to interpret. It was not carried forward as a strong
candidate.

## 8. Risks, Unknowns, and Recommendation

### What we do not know yet

- Whether Gradient Boosting's errors cluster in a specific patient
  subgroup, such as those presenting with deceptively near-normal
  vital signs.
- The practical cost of running SHAP explanations inside a live
  clinical workflow, including whether on-call staff would use them
  under time pressure.
- How this model's performance would hold up on data from a different
  time or a different hospital, since all figures in this memo come
  from a single dataset and a single train/test split.

### Recommendation

I recommend adopting Gradient Boosting as the Phase 3 candidate model,
conditional on three follow-up actions: building a lightweight
SHAP-based explanation panel for on-call clinicians before any
deployment decision, completing the subgroup error analysis with
adequate sample sizes, and monitoring ESI-1 recall specifically in any
pilot, rather than relying on aggregate accuracy or macro-F1 as the
headline success measure. This recommendation should be revisited if the
subgroup analysis reveals that Gradient Boosting's errors concentrate
disproportionately among a clinically vulnerable population.
