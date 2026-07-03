# Retail Sales KPI Reporting Platform

A full ETL-to-dashboard analytics project simulating a real business intelligence engagement: a retail business needs visibility into sales performance, and this project delivers a validated, automated reporting solution — end to end.

Built to demonstrate the same workflow used in enterprise BI/BA roles: requirements gathering → data engineering → validation → KPI reporting → stakeholder-ready dashboard.

## Business Problem

*(Framed as if written for a real stakeholder — this is the requirements-gathering skill BAs are hired for.)*

A retail operations team needs a recurring view of sales performance across regions, product categories, and time periods to support inventory and marketing decisions. Today reporting is manual, inconsistent, and error-prone. This project delivers an automated pipeline and dashboard that answers:

- Which regions/categories are driving revenue growth or decline?
- What are our top and bottom performing products?
- How does performance trend month over month?
- Where is data quality at risk (missing values, duplicate orders, outliers)?

See [`docs/business_requirements.md`](docs/business_requirements.md) for the full requirements doc.

## Architecture

```
Raw CSV data  →  Python ETL (extract/transform/load)  →  SQLite database
                        ↓
                data validation checks
                        ↓
              SQL KPI queries  →  Power BI dashboard
```

## Tech Stack

- **Python** (pandas) — extraction, transformation, validation
- **SQL** (SQLite for local dev, portable to SQL Server/Snowflake) — KPI queries
- **Power BI** — executive dashboard
- **pytest** — data validation testing

## Repo Structure

```
retail-kpi-reporting-platform/
├── data/
│   ├── raw/              # source data (not committed if large — see .gitignore)
│   └── processed/        # cleaned, validated output
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── validate.py
├── sql/
│   ├── schema.sql
│   └── kpi_queries.sql
├── dashboard/
│   ├── retail_kpi_dashboard.pbix   # Power BI file
│   └── screenshots/                # exported views for GitHub (pbix doesn't render inline)
├── docs/
│   ├── business_requirements.md
│   └── data_dictionary.md
├── tests/
│   └── test_validate.py
└── requirements.txt
```

## How to Run

```bash
pip install -r requirements.txt
python etl/extract.py
python etl/transform.py
python etl/validate.py
python etl/load.py
```

Then open `sql/kpi_queries.sql` against the resulting database, or open the Power BI file in `dashboard/` (connect it to `data/processed/retail.db`).

## Dashboard Preview

*(Screenshots go in `dashboard/screenshots/` — add these once the dashboard is built, so this section renders inline for anyone browsing the repo without Power BI installed.)*

## Key KPIs Delivered

- Revenue by region / category / month
- Top & bottom 10 products by revenue
- Month-over-month growth %
- Order volume vs. average order value
- Data quality scorecard (% records passing validation)

## Data Source

[Dataset link — see setup notes below]

## Status

🚧 In progress — see commit history for build log.
