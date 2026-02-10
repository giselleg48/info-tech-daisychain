from google.cloud import bigquery


PROJECT_ID = 'insert project id here'
TABLE_ID = 'insert table id here'
client = bigquery.Client(project=PROJECT_ID)

query = f"""
SELECT * FROM `{PROJECT_ID}.{TABLE_ID}`
LIMIT 10
"""

print("Querying")
df = client.query(query).to_dataframe(create_bqstorage_client=False)
print(df.head())