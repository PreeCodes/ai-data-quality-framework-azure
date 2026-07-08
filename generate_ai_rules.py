# Uses Claude AI to automatically generate 15 data quality rules 
import anthropic
import pandas as pd
import json 
import os

# Initialise Anthropic client using API key from .env file 
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
# Load the full cleaned UK retail dataset 
df = pd.read_csv('data/fact_sales_sample.csv')

# Build schema dictionary to send to Claude AI 
schema = {'table': 'fact_sales', 'columns': {c: str(df[c].dtype) for c in df.columns}, 'null_counts': df.isnull().sum().to_dict(), 'row_count': len(df), 'sample_values': {c: str(df[c].dropna().head(3).tolist()) for c in list(df.columns)[:5]}}

# Send schema to Claude AI and request 15 specific quality rules 
response = client.messages.create(
model='claude-opus-4-5',
max_tokens=1500,
messages=[{'role': 'user', 'content': 'You are a senior data quality engineer. Analyse this table schema and generate 15 specific data quality rules. Include null checks, range checks, uniqueness checks, referential integrity and business logic rules. Format as a numbered list. Schema: ' + json.dumps(schema)}]
)

# Extract text response from Claude API response
rules = ""
for block in response.content: 
    if block.type == "text": 
        rules = block.text 
        break
print('AI-Generated Quality Rules:')
print(rules)

# Save generated rules to text file for future reference 
with open('ai_generated_rules.txt', 'w') as f:
    f.write(rules)
print('Rules saved to ai_generated_rules.txt')
