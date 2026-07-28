"""
tests/test_data.py — Task 4(a): data-loading test that checks the expected schema.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data import VITALS, clean


def _make_raw_frame(n=200, seed=0):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "Unnamed: 0": range(n),
        "esi": rng.choice([1, 2, 3, 4, 5, np.nan, 9], size=n),
        "gender": rng.choice(["Male", "female", "F", "m", "MALE"], size=n),
        "age": rng.integers(1, 95, size=n).astype(float),
    })
    for col in VITALS:
        df[col] = rng.normal(loc=100, scale=20, size=n)
    df.loc[0, "triage_vital_temp"] = 150.0
    df.loc[1, "triage_vital_o2"] = 250.0
    return df


def test_clean_produces_valid_schema():
    raw = _make_raw_frame()
    df = clean(raw)

    assert df["esi"].isin([1, 2, 3, 4, 5]).all()
    for col in VITALS:
        assert df[col].isna().sum() == 0
    assert set(df["gender"].unique()) <= {0, 1}
    assert "Unnamed: 0" not in df.columns
    assert len(df) <= len(raw)
