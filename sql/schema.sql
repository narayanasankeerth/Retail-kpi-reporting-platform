-- Schema reference (SQLite created automatically by etl/load.py via pandas.to_sql;
-- this file documents the intended structure for portability to SQL Server/Snowflake)

CREATE TABLE IF NOT EXISTS orders_clean (
    order_id        TEXT,
    order_date      DATE,
    customer_id     TEXT,
    region          TEXT,
    category        TEXT,
    sub_category    TEXT,
    product_name    TEXT,
    sales           REAL,
    quantity        INTEGER,
    discount        REAL,
    profit          REAL
);

CREATE TABLE IF NOT EXISTS data_quality_log (
    check_name   TEXT,
    rows_failed  INTEGER,
    pct_failed   REAL
);
