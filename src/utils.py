"""
src/utils.py — shared helpers used by scripts/train.py and tests/.
"""

import random

import numpy as np
import yaml


def load_config(path):
    """Load config.yaml into a plain dict."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def set_seed(seed):
    """Fix random_state everywhere reasonable, so reruns are reproducible."""
    random.seed(seed)
    np.random.seed(seed)
