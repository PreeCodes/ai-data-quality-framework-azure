# AI-Powered Data Quality Framework on Azure Synapse

## What makes this different
Claude AI analyses the table schema and auto-generates 15 tailored data quality rules. Those rules are then implemented in Python and run automatically via GitHub Actions CI/CD on every code push.

## Source Data 
This project uses the **UCI Online Retail II dataset** — real UK retail transaction data containing 1 million+ rows of invoice records from a UK-based online retailer (2009-2011). 

### How to get the data 
1. Download from UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/502/online+retail+ii 
2. Extract the Excel file 
3. Save as CSV in your Project 1 folder: uk-retail-sales-dwh-ai/online_retail_II.csv 
4. Run save_sample.py to generate cleaned sample: python save_sample.py 
5. Run create_test_sample.py to generate test sample: python create_test_sample.py 

### Why data is not in this repo
The full dataset is 75MB — too large for GitHub. The 1000-row test sample in data/test_sample.csv contains real data for CI/CD pipeline testing.

## How AI rule generation works
1. Claude reads the table schema (columns, types, sample values, null counts)
2. Claude generates 15 specific quality rules tailored to the data
3. You implement those rules in Python
4. Rules run automatically on every commit

# Data Quality Rules for `fact_sales` Table (**Sample AI-generated rules from Claude**)

Based on the schema analysis, here are 15 specific data quality rules:

---

## Null Checks
1. **NULL_001**: `Invoice` must NOT be null (primary transaction identifier required for all sales records)

2. **NULL_002**: `Customer_ID` must NOT be null for non-cancelled invoices (essential for customer analytics; current float64 type suggests potential null handling issues)

3. **NULL_003**: `StockCode` must NOT be null (required to link to product dimension)

---

## Range Checks
4. **RANGE_001**: `Price` must be >= 0 (unit price cannot be negative; zero allowed for promotional items)

5. **RANGE_002**: `Quantity` must be between -1000 and 10000 (negative values indicate returns; extreme values suggest data entry errors)

6. **RANGE_003**: `InvoiceDate` must be within valid business period (between '2009-01-01' and CURRENT_DATE; no future dates allowed)

7. **RANGE_004**: `Revenue` must be within range -100000 to 1000000 (outliers beyond this suggest calculation errors or data corruption)

---

## Uniqueness Checks
8. **UNIQUE_001**: Combination of `Invoice` + `StockCode` should be unique per line item (no duplicate products on same invoice line)

9. **UNIQUE_002**: `Invoice` values should follow sequential or defined pattern with no unexpected gaps exceeding 1000

---

## Referential Integrity
10. **REF_001**: `Customer_ID` must exist in `dim_customer` table (orphan records indicate missing master data)

11. **REF_002**: `StockCode` must exist in `dim_product` table (all products sold must be in product master)

12. **REF_003**: `Country` must exist in `dim_geography` or match ISO country standard list

---

## Business Logic Rules
13. **BUS_001**: `Revenue` must equal `Quantity × Price` (tolerance ±0.01 for rounding; formula: `ABS(Revenue - (Quantity * Price)) <= 0.01`)

14. **BUS_002**: Cancelled invoices (typically starting with 'C' prefix when cast to string) must have negative `Quantity` and negative `Revenue` values

15. **BUS_003**: `InvoiceDate` format must be valid ISO timestamp ('YYYY-MM-DD HH:MM:SS') and parseable; all records within same `Invoice` must share identical `InvoiceDate`

---

## Summary Matrix

| Category | Count | Critical |
|----------|-------|----------|
| Null Checks | 3 | High |
| Range Checks | 4 | Medium |
| Uniqueness | 2 | High |
| Referential Integrity | 3 | High |
| Business Logic | 3 | Critical |

## Tech stack
- Python, pandas, anthropic
- dbt SQL transformation models
- GitHub Actions CI/CD
- Azure Synapse Analytics

## Architecture
Schema analysis → Claude AI rules → Python validation → dbt transforms → GitHub Actions auto-run

## Setup 
1. Clone this repository: git clone https://github.com/PreeCodes/ai-data-quality-framework-azure.git cd ai-data-quality-framework-azure 
2. Install required libraries: pip install pandas anthropic python-dotenv dbt-synapse 
3. Download source data and follow steps in Source Data section above 
4. Replace ANTHROPIC_API_KEY in generate_ai_rules.py with your actual key

### CI/CD Pipeline 
Every push to main branch automatically runs: python run_quality_checks.py 
Results are visible in the GitHub Actions tab.