"""
extract.py
Pulls raw sales data into data/raw/ for downstream processing.

Setup:
    Download a retail sales dataset (e.g. Kaggle's "Sample Superstore" or
    the Olist Brazilian E-Commerce dataset) and place the CSV at:
        data/raw/orders_raw.csv

    This script is intentionally simple for v1 — it validates the file
    exists and does a basic structural check. In a real pipeline this is
    where you'd add API calls, database connections, or S3 pulls.
"""

import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path(__file__).parent.parent / "data" / "raw" / "orders_raw.csv"


def extract() -> pd.DataFrame:
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Expected raw data at {RAW_DATA_PATH}. "
            "Download a retail sales dataset and place it there. "
            "See README.md 'Data Source' section for a recommended dataset."
        )

    df = pd.read_csv(RAW_DATA_PATH)
    print(f"Extracted {len(df)} rows, {len(df.columns)} columns from {RAW_DATA_PATH.name}")
    return df


if __name__ == "__main__":
    df = extract()
    print(df.head())
