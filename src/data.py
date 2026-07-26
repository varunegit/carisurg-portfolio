"""
src/data.py — load and clean the raw Yale EMMLC triage export.

Refactored from Week 7 notebook cells 3-4 ("Load and clean the raw data").
Logic is unchanged from the notebook; only reorganised into functions.
"""

import numpy as np
import pandas as pd

VITALS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
    "triage_glucose",
]


def load_raw(path):
    """Read the raw CSV export into a DataFrame."""
    df_raw = pd.read_csv(path)
    return df_raw


def clean(df_raw):
    """Turn the raw, messy export into a modelling-ready table.

    Steps (unchanged from Week 7 notebook cell 4):
      1. Drop stray index columns (e.g. "Unnamed: 0").
      2. Coerce vitals to numeric; unparseable values become NaN.
      3. Keep only rows with a valid ESI label (1-5).
      4. Blank out physically impossible vitals (temp, o2).
      5. Encode gender to 0/1.
      6. Fill remaining missing numeric values with the column median.
    """
    df = df_raw.copy()

    # 1) Drop any stray index column pandas adds on export
    df = df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")], errors="ignore")

    # 2) Force vitals to be numbers; unparseable text (e.g. "120bpm") becomes NaN
    for col in VITALS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 3) The ESI label must be 1-5. Drop rows where it is missing or out of range.
    df["esi"] = pd.to_numeric(df["esi"], errors="coerce")
    df = df[df["esi"].isin([1, 2, 3, 4, 5])].copy()

    # 4) Blank out physically impossible vitals so they don't poison the model
    df.loc[(df["triage_vital_temp"] < 90) | (df["triage_vital_temp"] > 110), "triage_vital_temp"] = np.nan
    df.loc[df["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    # 5) Encode gender to 0/1 (handles odd casings like "m" / "MALE")
    df["gender"] = (
        df["gender"].astype(str).str.strip().str.lower().map({"male": 0, "m": 0, "female": 1, "f": 1})
    )

    # 6) Fill remaining missing numeric values with the column median
    for col in VITALS + ["age", "gender"]:
        df[col] = df[col].fillna(df[col].median())

    df["esi"] = df["esi"].astype(int)
    return df


def select_xy(df, target="esi"):
    """Split a cleaned DataFrame into feature matrix X and target y.

    Excludes leakage columns (known only after triage), admin/arrival
    columns, and demographic columns (added back explicitly, if at all,
    via src/features.py::add_demographics).
    """
    demographics = [
        "age", "gender", "ethnicity", "race", "lang", "religion",
        "maritalstatus", "employstatus", "insurance_status",
    ]
    admin = ["dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin"]
    leakage = ["disposition", "previousdispo"]

    features = [c for c in df.columns if c != target and c not in leakage + admin + demographics]

    X = df[features]
    y = df[target]
    return X, y
