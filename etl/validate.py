"""
validate.py
Runs data quality checks on transformed data and produces a validation report.
This is the "requirements acceptance criteria" from docs/business_requirements.md,
implemented as code.
"""

import pandas as pd
from etl.transform import transform


def run_validation(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a DataFrame log of validation issues found, one row per issue type."""
    issues = []

    def log(check_name: str, condition_series: pd.Series):
        n_failed = int(condition_series.sum())
        issues.append({
            "check": check_name,
            "rows_failed": n_failed,
            "pct_failed": round(100 * n_failed / len(df), 2) if len(df) else 0,
        })

    if "sales" in df.columns:
        log("sales_negative_or_zero", df["sales"] <= 0)
        log("sales_missing", df["sales"].isna())

    if "quantity" in df.columns:
        log("quantity_negative_or_zero", df["quantity"] <= 0)

    if "discount" in df.columns:
        log("discount_out_of_range", ~df["discount"].between(0, 1))

    if "order_date" in df.columns:
        log("order_date_missing_or_invalid", df["order_date"].isna())

    if "order_id" in df.columns:
        log("order_id_missing", df["order_id"].isna())

    report = pd.DataFrame(issues)
    return report


def validate() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = transform()
    report = run_validation(df)

    print("\n=== Data Quality Report ===")
    print(report.to_string(index=False) if not report.empty else "No checks run (missing expected columns).")

    total_issue_pct = report["pct_failed"].sum() if not report.empty else 0
    print(f"\nOverall data quality score: {max(0, round(100 - total_issue_pct, 2))}%")

    return df, report


if __name__ == "__main__":
    validate()
