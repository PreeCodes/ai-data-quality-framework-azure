# Loads raw UK retail data from Project 1 and prepares it 
import pandas as pd
import os

# Load raw CSV from Project 1 folder
df = pd.read_csv('../uk-retail-sales-dwh-ai/online_retail_II.csv', encoding='latin1')
# Remove rows with missing Customer ID 
df_clean = df.dropna(subset=['Customer ID']).copy()
# Remove cancelled/returned orders (negative quantity) 
df_clean = df_clean[df_clean['Quantity'] > 0]
 # Calculate Revenue as Quantity multiplied by Price 
df_clean['Revenue'] = df_clean['Quantity'] * df_clean['Price']
# Rename columns — replace spaces with underscores 
df_clean.columns = [c.replace(' ', '_') for c in df_clean.columns]
# Create data folder if it doesn't exist 
os.makedirs('data', exist_ok=True)
# Save cleaned dataset for quality checks and sampling 
df_clean.to_csv('data/fact_sales_sample.csv', index=False)
print('Sample saved: ' + str(len(df_clean)) + ' rows')
