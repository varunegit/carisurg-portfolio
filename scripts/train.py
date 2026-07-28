"""
scripts/train.py — the one command that trains the pinned final model.

Usage:
    python scripts/train.py --config config.yaml
"""

import argparse
import sys
from pathlib import Path

from sklearn.model_selection import train_test_split

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data import clean, load_raw, select_xy
from src.features import add_clinical_features, add_demographics
from src.model import build_model, evaluate, fit_and_time
from src.utils import load_config, set_seed


def main():
    parser = argparse.ArgumentParser(description="Train the pinned CariSurg triage model.")
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    set_seed(cfg["seed"])

    print(f"Loading data from {cfg['data']['raw_path']} ...")
    df_raw = load_raw(cfg["data"]["raw_path"])
    df = clean(df_raw)
    X, y = select_xy(df, target=cfg["data"]["target"])

    split_cfg = cfg.get("train_test_split", {})
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=split_cfg.get("test_size", 0.2),
        stratify=y if split_cfg.get("stratify", True) else None,
        random_state=cfg["seed"],
    )

    X_train_fe = add_clinical_features(X_train)
    X_test_fe = add_clinical_features(X_test)

    if cfg.get("use_demographics", False):
        X_train_fe = add_demographics(X_train_fe, df)
        X_test_fe = add_demographics(X_test_fe, df)

    model_name = cfg["final_model"]
    model_params = cfg["models"][model_name]
    print(f"Building and training '{model_name}' ...")
    model = build_model(model_name, model_params, cfg["seed"])
    model, train_time_s = fit_and_time(model, X_train_fe, y_train)

    metrics = evaluate(model, X_test_fe, y_test)
    metrics["Train (s)"] = train_time_s

    print("\nHeld-out test metrics:")
    for k, v in metrics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
