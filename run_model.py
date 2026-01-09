#!/usr/bin/env python3
"""
Usage:
    python run_model.py --input "[5.1, 3.5, 1.4, 0.2]"
"""

import argparse
import json
from pathlib import Path
import numpy as np
import joblib

MODEL_PATH = Path("artifacts/model.pkl")

# class mapping
CLASS_NAMES = ["I am setosa", "I am versicolor", "I am virginica"]

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        required=True,
        help="Feature list as JSON string. Example: \"[5.1,3.5,1.4,0.2]\""
    )
    args = parser.parse_args()

    # parse input
    try:
        features = json.loads(args.input)
    except json.JSONDecodeError:
        raise ValueError("Invalid input. Use JSON list, e.g. --input \"[5.1,3.5,1.4,0.2]\"")

    X = np.array(features).reshape(1, -1)

    model = load_model()
    pred_class = int(model.predict(X)[0])
    pred_name = CLASS_NAMES[pred_class]

    print(json.dumps({
        "prediction": pred_class,
        "flower": pred_name
    }))

if __name__ == "__main__":
    main()
