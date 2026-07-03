"""
load.py
Loads cleaned data into a local SQLite database (portable to SQL Server / Snowflake
later by swapping the connection string — schema.sql is written in standard SQL).
"""

import sqlite3
from pathlib import Path
from etl.validate import validate

DB_PATH = Path(__file__).parent.parent / "data" / "processed" / "retail.db"


def load():
    df, report = validate()

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    df.to_sql("orders_clean", conn, if_exists="replace", index=False)
    report.to_sql("data_quality_log", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print(f"\nLoaded {len(df)} rows into {DB_PATH}")
    print("Tables: orders_clean, data_quality_log")


if __name__ == "__main__":
    load()
