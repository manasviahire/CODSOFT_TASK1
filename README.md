# CODSOFT_TASK1
DATA CLEANING &amp; PREPROCESSING
# Import Pandas
import pandas as pd

# Step 1: Load the dataset
# Replace 'dataset.csv' with your file name
df = pd.read_csv("dataset.csv")

# Step 2: Inspect the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nSummary Statistics:")
print(df.describe(include='all'))

# Step 3: Identify missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Identify duplicate records
duplicates = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicates)

# Step 5: Check data types
print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Data Cleaning
# -----------------------------

# Step 6: Remove duplicate rows
df = df.drop_duplicates()

# Step 7: Handle missing values

# Fill missing values in numeric columns with the median
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing values in categorical columns with the mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

# Step 8: Remove extra spaces from text columns
for col in categorical_cols:
    df[col] = df[col].str.strip()

# Step 9: Convert data types where necessary

# Example: Convert a date column (change column name if needed)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Example: Convert Age column to integer (if present)
if 'Age' in df.columns:
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)

# Step 10: Check cleaned dataset
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\nUpdated Data Types:")
print(df.dtypes)

# Step 11: Save the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as 'cleaned_dataset.csv'.")
