"""
transform.py
Cleans and standardizes raw sales data.

NOTE: Column names below assume a Superstore-style dataset (order_id, order_date,
region, category, sub_category, product_name, sales, quantity, discount, profit).
Adjust column mapping in `standardize_columns()` if using a different dataset.
"""

import pandas as pd
from etl.extract import extract


COLUMN_MAP = {
    # left = expected raw name variants -> right = standardized name
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Region": "region",
    "Category": "category",
    "Sub-Category": "sub_category",
    "Product Name": "product_name",
    "Sales": "sales",
    "Quantity": "quantity",
    "Discount": "discount",
    "Profit": "profit",
}


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={k: v for k, v in COLUMN_MAP.items() if k in df.columns})
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_columns(df)

    # Parse dates
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Drop exact duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    print(f"Dropped {before - len(df)} exact duplicate rows")

    # Basic type coercion for numeric fields
    for col in ["sales", "quantity", "discount", "profit"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def transform() -> pd.DataFrame:
    raw = extract()
    cleaned = clean(raw)
    print(f"Transform complete: {len(cleaned)} rows remain")
    return cleaned


if __name__ == "__main__":
    df = transform()
    print(df.head())
