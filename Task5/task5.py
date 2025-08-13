import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Pranai Kumar\\Downloads\\Sales Dataset.csv")
df['Order Date']=pd.to_datetime(df['Order Date'])
print(df.info())
print(df.describe())
for col in df.select_dtypes(include='object').columns:
    print("")
    print("hello")
    print(df[col].value_counts())
print("sum and duplicates")    
print(df.isnull().sum())
print(df.drop_duplicates(inplace=True))
sns.set(style='darkgrid')
df.hist(bins=100, figsize=(12,8))
plt.suptitle('Histograms of Numerical Features')
plt.show()
plt.figure(figsize=(12,6))
sns.boxplot(data=df.select_dtypes(include='number'))
plt.title('Boxplots of Numerical Features')
plt.show()
#scatter plot
sns.scatterplot(x='Amount', y='Profit',color='red', data=df)
plt.title('Scatterplot: feature1 vs feature2')
plt.show()
#pairplot
sns.pairplot(df)
plt.suptitle('Pairplot of object Features', y=1.02)
plt.show()
#heatmaps
plt.figure(figsize=(10,8))
sns.heatmap(data=df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()



