"""
Unit tests for the validation logic. Run with: pytest
These don't require the real dataset — they test the validation rules
against small synthetic DataFrames.
"""

import pandas as pd
from etl.validate import run_validation


def test_flags_negative_sales():
    df = pd.DataFrame({"sales": [10, -5, 0, 20]})
    report = run_validation(df)
    row = report[report["check"] == "sales_negative_or_zero"].iloc[0]
    assert row["rows_failed"] == 2


def test_flags_missing_sales():
    df = pd.DataFrame({"sales": [10, None, 20, None]})
    report = run_validation(df)
    row = report[report["check"] == "sales_missing"].iloc[0]
    assert row["rows_failed"] == 2


def test_flags_discount_out_of_range():
    df = pd.DataFrame({"discount": [0.1, 1.5, -0.2, 0.5]})
    report = run_validation(df)
    row = report[report["check"] == "discount_out_of_range"].iloc[0]
    assert row["rows_failed"] == 2


def test_no_false_positives_on_clean_data():
    df = pd.DataFrame({
        "sales": [10, 20, 30],
        "quantity": [1, 2, 3],
        "discount": [0.1, 0.0, 0.2],
    })
    report = run_validation(df)
    assert report["rows_failed"].sum() == 0
