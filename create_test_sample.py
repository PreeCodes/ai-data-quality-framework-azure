# Creates a small 1000-row sample from the full cleaned dataset 
# This sample is used by GitHub Actions CI/CD pipeline for quality checks
import pandas as pd 

# Load the full cleaned dataset 
df = pd.read_csv('data/fact_sales_sample.csv') 
# Randomly sample 1000 rows with fixed seed for reproducibility
sample = df.sample(1000, random_state=42) 
# Save sample to data folder for GitHub Actions to use
sample.to_csv('data/test_sample.csv', index=False) 
print('Sample created:', len(sample), 'rows') 