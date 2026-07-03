-- KPI Queries
-- Run against data/processed/retail.db
-- These map directly to the acceptance criteria in docs/business_requirements.md

-- 1. Revenue by region, category, month
SELECT
    strftime('%Y-%m', order_date) AS month,
    region,
    category,
    ROUND(SUM(sales), 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS order_count,
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM orders_clean
GROUP BY month, region, category
ORDER BY month, total_revenue DESC;


-- 2. Top 10 products by revenue
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_revenue,
    SUM(quantity) AS units_sold
FROM orders_clean
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 10;


-- 3. Bottom 10 products by revenue (excluding zero-sale noise)
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_revenue,
    SUM(quantity) AS units_sold
FROM orders_clean
WHERE sales > 0
GROUP BY product_name
ORDER BY total_revenue ASC
LIMIT 10;


-- 4. Month-over-month revenue growth %
WITH monthly AS (
    SELECT
        strftime('%Y-%m', order_date) AS month,
        SUM(sales) AS total_revenue
    FROM orders_clean
    GROUP BY month
)
SELECT
    month,
    total_revenue,
    ROUND(
        100.0 * (total_revenue - LAG(total_revenue) OVER (ORDER BY month))
        / NULLIF(LAG(total_revenue) OVER (ORDER BY month), 0),
        2
    ) AS mom_growth_pct
FROM monthly
ORDER BY month;


-- 5. Data quality scorecard
SELECT
    check_name,
    rows_failed,
    pct_failed
FROM data_quality_log
ORDER BY pct_failed DESC;
