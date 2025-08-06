import pandas as pd
df=pd.read_csv("C:\\Users\\Pranai Kumar\\Downloads\\amazon.csv")
df.info()
df.describe()
print(df.isna().sum())
df.drop_duplicates(inplace=True)
df_cleaned = df.drop_duplicates()
print(df_cleaned)
df.to_csv('C:\\Users\\Pranai Kumar\\Downloads\\your_dataset_cleaned.csv', index=False)