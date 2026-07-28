"""
tests/test_pipeline.py — Task 4(b): training smoke test on ~50-60 rows.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data import VITALS, clean, select_xy
from src.features import add_clinical_features
from src.model import build_model


def _tiny_clean(n=60, seed=1):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "esi": rng.choice([1, 2, 3, 4, 5], size=n),
        "gender": rng.choice(["Male", "Female"], size=n),
        "age": rng.integers(1, 95, size=n).astype(float),
        "ethnicity": rng.choice(["Hispanic or Latino", "Non-Hispanic"], size=n),
        "race": rng.choice(["White or Caucasian", "Black or African American"], size=n),
        "lang": "English",
        "religion": "Other",
        "maritalstatus": "Single",
        "employstatus": "Employed",
        "insurance_status": "Insured",
        "dep_name": "A",
        "arrivalmode": "Walk-in",
        "arrivalmonth": 1,
        "arrivalday": 1,
        "arrivalhour_bin": "morning",
        "disposition": "Admit",
        "previousdispo": "Discharge",
    })
    for col in VITALS:
        df[col] = rng.normal(loc=100, scale=15, size=n)
    return df


def test_smoke_train_predict():
    raw = _tiny_clean(60)
    df = clean(raw)
    X, y = select_xy(df)
    X_fe = add_clinical_features(X)

    assert "disposition" not in X_fe.columns
    assert "previousdispo" not in X_fe.columns

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X_fe, y, test_size=0.3, random_state=42
    )

    model = build_model("gradient_boosting", {"max_iter": 20}, seed=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    assert len(preds) == len(y_test)
