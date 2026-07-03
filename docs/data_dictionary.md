# Data Dictionary

*Fill this in once the dataset is finalized (see setup notes in README). Template below assumes an order-line-level sales dataset (e.g. Superstore-style or Olist-style data).*

## Raw Table: `orders_raw`

| Column | Type | Description | Notes |
|---|---|---|---|
| order_id | string | Unique order identifier | |
| order_date | date | Date order was placed | |
| customer_id | string | Unique customer identifier | |
| region | string | Sales region | |
| category | string | Product category | |
| sub_category | string | Product sub-category | |
| product_name | string | Product name | |
| sales | float | Revenue for the line item | Validate: must be > 0 |
| quantity | integer | Units sold | Validate: must be > 0 |
| discount | float | Discount applied (0–1) | Validate: 0 <= discount <= 1 |
| profit | float | Profit for the line item | Can be negative |

## Processed Table: `orders_clean`

Same schema as raw, after:
- Duplicate `order_id` + line item removal
- Null handling (documented per column)
- Outlier flagging (sales/profit beyond 3 std dev, flagged not dropped)

## Derived KPI Tables

- `kpi_monthly_revenue` — revenue, order count, AOV by month/region/category
- `kpi_top_products` — top/bottom 10 products by revenue
- `data_quality_log` — row-level validation failures with reason codes
