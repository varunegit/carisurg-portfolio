"""
src/model.py — build a model from config, train it, and evaluate it
on the six benchmark axes used in docs/model-selection.md.

Refactored from Week 7 notebook cells 10-11, 14, 17, 19, 21, 25-26.
"""

import time

from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, recall_score
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

MODEL_BUILDERS = {
    "logistic_regression": lambda p, seed: make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=p.get("max_iter", 1000), random_state=seed)
    ),
    "decision_tree": lambda p, seed: DecisionTreeClassifier(random_state=seed),
    "random_forest": lambda p, seed: RandomForestClassifier(
        n_estimators=p.get("n_estimators", 300),
        max_depth=p.get("max_depth"),
        min_samples_leaf=p.get("min_samples_leaf", 1),
        max_features=p.get("max_features", "sqrt"),
        class_weight=p.get("class_weight", "balanced"),
        random_state=seed,
        n_jobs=-1,
    ),
    # alias: same builder, used for the RandomizedSearchCV-tuned hyperparameters
    "random_forest_tuned": lambda p, seed: RandomForestClassifier(
        n_estimators=p.get("n_estimators", 300),
        max_depth=p.get("max_depth"),
        min_samples_leaf=p.get("min_samples_leaf", 1),
        max_features=p.get("max_features", "sqrt"),
        class_weight=p.get("class_weight", "balanced"),
        random_state=seed,
        n_jobs=-1,
    ),
    "gradient_boosting": lambda p, seed: HistGradientBoostingClassifier(
        max_depth=p.get("max_depth", 6),
        learning_rate=p.get("learning_rate", 0.1),
        max_iter=p.get("max_iter", 300),
        class_weight=p.get("class_weight", "balanced"),
        random_state=seed,
    ),
    "mlp": lambda p, seed: make_pipeline(
        StandardScaler(),
        MLPClassifier(
            hidden_layer_sizes=tuple(p.get("hidden_layer_sizes", [64, 32])),
            alpha=p.get("alpha", 1e-3),
            max_iter=p.get("max_iter", 500),
            random_state=seed,
        ),
    ),
}


def build_model(name, params, seed):
    """Construct an unfitted model/pipeline for `name` using `params` from config.yaml."""
    if name not in MODEL_BUILDERS:
        raise ValueError(f"Unknown model '{name}'. Options: {list(MODEL_BUILDERS)}")
    return MODEL_BUILDERS[name](params or {}, seed)


def evaluate(model, X_test, y_test, esi1_label=1):
    """Score a fitted model on accuracy, ESI-1 recall, macro-F1, and inference time."""
    t0 = time.perf_counter()
    preds = model.predict(X_test)
    infer_ms = (time.perf_counter() - t0) / len(X_test) * 1000  # per prediction

    return {
        "Accuracy": round(accuracy_score(y_test, preds), 3),
        "Recall ESI 1": round(
            recall_score(y_test, preds, labels=[esi1_label], average=None, zero_division=0)[0], 3
        ),
        "Macro F1": round(f1_score(y_test, preds, average="macro"), 3),
        "Infer (ms/pred)": round(infer_ms, 3),
    }


def fit_and_time(model, X_train, y_train):
    """Fit a model and return (fitted_model, train_time_seconds)."""
    t0 = time.perf_counter()
    model.fit(X_train, y_train)
    return model, round(time.perf_counter() - t0, 2)
