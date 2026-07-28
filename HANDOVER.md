# Handover Document — CariSurg Triage Model

## 1. Project summary
This project predicts a patient's Emergency Severity Index (ESI, 1-5) at
the moment of ED triage, using vitals and clinical red-flag features from
the Yale EMMLC dataset. It is intended as a decision-support signal for
front-door triage staff at Mercer General Hospital — not a replacement for
clinical judgement. Primary stakeholders: Dr. De Freitas, Dr. Reyes
(clinical safety), and Martina Griffith (Clinical IT/Governance).

## 2. Final-model decision
**We ship Gradient Boosting.** It ties the tuned Random Forest on ESI-1
recall (0.312) — the clinical safety metric Dr. Reyes prioritises — at
roughly 1/38th the training cost (9.51s vs 365.03s) and the lowest
inference time of any model tested (0.015 ms/pred). This is conditional on
adding a SHAP-based explanation panel before any deployment consideration,
to offset its lower interpretability (Low vs Medium for Random Forest).
Full reasoning: `docs/decisions/2026-week-7-model-choice.md`.

## 3. How to run
```
git clone https://github.com/varunegit/carisurg-portfolio.git
cd carisurg-portfolio
pip install -r requirements.txt
python scripts/train.py --config config.yaml
```
Place the raw dataset at `data/yaleemmlc_admissionprediction_triage.csv`
before running (see §4 — the file is git-ignored and not included in this
public repo).

## 4. Where the data lives
- Path: `data/yaleemmlc_admissionprediction_triage.csv` (git-ignored, not
  committed — per README, to protect against data leaks).
- Governance status: de-identified Yale EMMLC export used for educational
  and research purposes. De-identified does **not** mean ungoverned — the
  file must not be redistributed, and access should be limited to those
  working directly on this project. Confirm formal data-sharing terms with
  Martina Griffith before any production or multi-site use.

## 5. Known limitations
1. **Single-site data.** Yale EMMLC only — distribution shift is likely if
   applied to Mercer's own patient population without local validation.
2. **ESI-1 recall is still modest (0.312) even for the best candidate.**
   The model is a support signal, not a substitute for clinical triage
   judgement, and roughly two-thirds of true ESI-1 cases would still be
   missed on this test split.
3. **Demographics excluded from the feature set by design** (fairness
   decision, Weeks 5-6). `add_demographics()` exists in `src/features.py`
   but is off by default (`use_demographics: false` in `config.yaml`).
4. **Recall stability is unconfirmed.** Per the decision journal, the
   0.312 ESI-1 recall figure comes from a single train/test split with a
   very small number of ESI-1 encounters in the test set — it has not yet
   been validated across multiple splits or with bootstrapped confidence
   intervals.

## 6. Who to ask
- **Model / pipeline questions:** Varune Joseph (author) — github.com/varunegit
- **Clinical safety / ESI-1 recall priority:** Dr. Reyes
- **Data governance / deployment:** Martina Griffith
- **Refactor / engineering questions:** Nile Anderson (Week 8 Tutorial 2)
- **Original project sponsor:** Dr. De Freitas
