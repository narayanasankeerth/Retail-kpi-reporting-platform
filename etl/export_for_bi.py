"""
export_for_bi.py
Exports cleaned data from retail.db into CSV format for Power BI to consume.
"""

import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "processed" / "retail.db"
OUTPUT_PATH = Path(__file__).parent.parent / "data" / "processed" / "orders_clean.csv"

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM orders_clean", conn)
conn.close()

df.to_csv(OUTPUT_PATH, index=False)
print(f"Exported {len(df)} rows to {OUTPUT_PATH}")