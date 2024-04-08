import pandas as pd

#The most commonly used functions for loading data are pd.read_csv(),
# pd.read_excel(), pd.read_sql(), pd.read_json(), etc.

# 1. Loading Data
# Load a sample CSV file containing sales transactions data
df = pd.read_csv('sample_data.csv')

# 2. Inspecting Data
# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display the last few rows of the DataFrame
print("\nLast few rows of the DataFrame:")
print(df.tail())

# Display information about the DataFrame
print("\nInformation about the DataFrame:")
print(df.info())

# Display summary statistics of the DataFrame
print("\nSummary statistics of the DataFrame:")
print(df.describe())

# Display data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Display the shape of the DataFrame (number of rows and columns)
print("\nShape of the DataFrame (number of rows and columns):", df.shape)
