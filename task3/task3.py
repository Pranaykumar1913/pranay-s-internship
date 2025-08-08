f.info()
print(df.head())
#print(df.isna().sum())
df.drop_duplicates(inplace=True)
print(df.isnull().values.any())
df['reviewText'] = df['reviewText'].fillna("Unknown")

# See total number of missing values
print(df.isnull().sum().sum())
print(df.isna().sum())

df.to_csv(r"C:\Users\Pranai Kumar\OneDrive\Desktop\vscode py\task3\amazon_review_cl.csv", index=False)
