import pandas as pd
df = pd.read_csv('C:\\Users\\Pranai Kumar\\OneDrive\\Documents\\car_prices.csv')
#print(df.head())     # Gives First 5 rows
#print(df.info())     # Data types and missing values info
#print(df.describe()) # Summary statistics for numeric columns
print(df.isna().sum())  # Count missing values per column
df.drop_duplicates(inplace=True)
print (df)
df['make'] = df['make'].str.lower().str.strip()
#print(df['make'].unique())
# Convert to datetime
df['saledate'] = pd.to_datetime(df['saledate'], dayfirst=True, errors='coerce')
print(df)

df.to_csv('your_dataset_cleaned.csv', index=False)