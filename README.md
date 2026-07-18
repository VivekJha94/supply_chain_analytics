# Supply Chain Analytics Project

## Business Problem
Why are delivery delays increasing and where is cost leakage 
happening across our supply chain?

## Tools Used
- Python (Pandas, Matplotlib, Seaborn) — EDA & data cleaning
- PostgreSQL (PgAdmin) — Business queries & insight extraction
- Power BI — Interactive 3-page dashboard

## Dataset
DataCo Supply Chain Dataset — 180,519 rows, 53 columns
Source: Kaggle

## Key Findings
1. **54.8% of all orders are delivered late** — a structural 
   problem consistent across all months and markets
2. **First Class shipping has a 95.3% late rate** — the most 
   expensive option is paradoxically the worst performer
3. **Blanket 10.14% discount applied across all departments** 
   — identified as the primary cost leakage driver
4. **Fan Shop alone absorbs $1.7M in discounts** across 
   customer segments, with only 10.5% avg margin
5. **No seasonal pattern in delays** — root cause is systemic,
   not demand-driven

## Dashboard Pages

### 1. Overview
<img width="1022" height="550" alt="overview" src="https://github.com/user-attachments/assets/9d022124-b80a-4f4f-9922-2b381fe220fc" />


### 2. Delivery Deep Dive
<img width="983" height="546" alt="delivery_deep_dive" src="https://github.com/user-attachments/assets/52aa354b-7690-434a-a95f-29a76df6f596" />


### 3. Profit & Cost Leakage
<img width="983" height="548" alt="profit_cost_leakage" src="https://github.com/user-attachments/assets/c697354a-5929-4165-b90c-ba8ebc1ee019" />

## Project Structure
- `notebooks/` — EDA and data cleaning in Python
- `sql/` — 5 business queries in PostgreSQL
- `dashboard/` — Power BI .pbix file
- `images/` — Dashboard screenshots
