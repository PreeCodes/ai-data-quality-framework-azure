# Runs 10 automated data quality rules against UK retail sample data 
import pandas as pd

# Load test sample — 1000 rows of real UK retail data 
df = pd.read_csv('data/test_sample.csv')
# Store results of each rule check 
results = []

def check(name, cond):
    # Evaluate condition and store pass/fail result
    ok = bool(cond)
    results.append({'rule': name, 'passed': ok})
    print(('PASSED: ' if ok else 'FAILED: ') + name)
    return ok

# Null checks — ensure critical columns have no missing values 
check('Revenue not null', df['Revenue'].notna().all())
# Range checks — ensure numeric values are within valid ranges 
check('Revenue positive', (df['Revenue'] >= 0).all())
check('Quantity at least 1', (df['Quantity'] >= 1).all())
check('Customer ID not null', df['Customer_ID'].notna().all())
# Volume check — ensure dataset meets minimum row threshold 
check('Row count above 100k', len(df) > 100000)
check('StockCode not null', df['StockCode'].notna().all())
# Revenue above 50000 may indicate bulk wholesale or data error 
check('Revenue below 50000', (df['Revenue'] <= 50000).all())
check('Invoice not null', df['Invoice'].notna().all())
check('Country not null', df['Country'].notna().all())
check('Price positive', (df['Price'] > 0).all())

# Print final scorecard summary 
passed = sum(1 for r in results if r['passed'])
print('Result: ' + str(passed) + '/10 rules PASSED')