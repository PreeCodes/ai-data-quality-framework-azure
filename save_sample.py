import pandas as pd
import os

df = pd.read_csv('../uk-retail-sales-dwh-ai/online_retail_II.csv', encoding='latin1')
df_clean = df.dropna(subset=['Customer ID']).copy()
df_clean = df_clean[df_clean['Quantity'] > 0]
df_clean['Revenue'] = df_clean['Quantity'] * df_clean['Price']
df_clean.columns = [c.replace(' ', '_') for c in df_clean.columns]
os.makedirs('data', exist_ok=True)
df_clean.to_csv('data/fact_sales_sample.csv', index=False)
print('Sample saved: ' + str(len(df_clean)) + ' rows')
