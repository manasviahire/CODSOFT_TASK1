import pandas as pd
import numpy as np
# Load dataset
df = pd.read_csv("Retail_Sales_EDA_Dataset.csv")

# Display first 5 rows
print(df.head())
print(df.info())
print("Rows and Columns:", df.shape)
print(df.describe())
duplicates = df.duplicated().sum()
print("Duplicate Records:", duplicates)
print(df.dtypes)
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].median())
df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].mean())
print(df.isnull().sum())
df = df.drop_duplicates()

print("Duplicates after cleaning:", df.duplicated().sum())
df['Customer_Age'] = df['Customer_Age'].astype(int)
df['Customer_Rating'] = df['Customer_Rating'].round(1)
df['Quantity'] = df['Quantity'].astype(int)
df['Delivery_Days'] = df['Delivery_Days'].astype(int)
print(df['Gender'].unique())
print(df['City'].unique())
print(df['Product_Category'].unique())
print(df['Payment_Method'].unique())
print(df['Returned'].unique())
text_columns = ['Gender','City','Product_Category','Payment_Method','Returned']
for col in text_columns:
    df[col] = df[col].str.strip().str.title()
print(df.info())
print(df.head())
print(df.describe())
df.to_csv("Retail_Sales_Cleaned.csv", index=False)
print("Cleaned dataset saved successfully.")
