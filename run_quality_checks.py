import pandas as pd

df = pd.read_csv('data/test_sample.csv')
results = []

def check(name, cond):
    ok = bool(cond)
    results.append({'rule': name, 'passed': ok})
    print(('PASSED: ' if ok else 'FAILED: ') + name)
    return ok

check('Revenue not null', df['Revenue'].notna().all())
check('Revenue positive', (df['Revenue'] >= 0).all())
check('Quantity at least 1', (df['Quantity'] >= 1).all())
check('Customer ID not null', df['Customer_ID'].notna().all())
check('Row count above 100k', len(df) > 100000)
check('StockCode not null', df['StockCode'].notna().all())
check('Revenue below 50000', (df['Revenue'] <= 50000).all())
check('Invoice not null', df['Invoice'].notna().all())
check('Country not null', df['Country'].notna().all())
check('Price positive', (df['Price'] > 0).all())

passed = sum(1 for r in results if r['passed'])
print('Result: ' + str(passed) + '/10 rules PASSED')