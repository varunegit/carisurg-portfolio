"""
src/features.py — engineer clinical features and (optionally) encode demographics.

Refactored from Week 7 notebook cells 12 and 15.
"""

import pandas as pd


def add_clinical_features(data):
    """Build red-flag clinical features from existing vitals."""
    out = data.copy()

    out["is_tachypneic"] = (out["triage_vital_rr"] > 20).astype(int)
    out["is_hypoxic"] = (out["triage_vital_o2"] < 92).astype(int)
    out["is_febrile"] = (out["triage_vital_temp"] >= 100.4).astype(int)
    out["is_bradycardic"] = (out["triage_vital_hr"] < 60).astype(int)

    out["red_flag_count"] = out[
        ["is_tachypneic", "is_hypoxic", "is_febrile", "is_bradycardic"]
    ].sum(axis=1)

    return out


def add_demographics(X_fe, df):
    """Bolt one-hot-encoded demographics onto an existing feature frame.

    OFF BY DEFAULT in the training pipeline (see config.yaml
    `use_demographics: false`) — a fairness decision from Week 5/6.
    """
    demo_1hot = pd.get_dummies(df[["ethnicity", "race"]], prefix=["eth", "race"], dtype=int)

    rows = X_fe.index
    extra = demo_1hot.loc[rows].copy()
    extra["age"] = df.loc[rows, "age"]
    extra["gender"] = df.loc[rows, "gender"]
    return pd.concat([X_fe, extra], axis=1)
