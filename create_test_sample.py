import pandas as pd 

df = pd.read_csv('data/fact_sales_sample.csv') 
sample = df.sample(1000, random_state=42) 
sample.to_csv('data/test_sample.csv', index=False) 
print('Sample created:', len(sample), 'rows') 