import pandas as pd

# Load sample data into a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, None, 40, 45],  # Including missing value
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston']
}
df = pd.DataFrame(data)

# 1. Data Filtering and Selection
# Selecting rows with Age greater than 30
print("Rows with Age greater than 30:")
print(df[df['Age'] > 30])

# Selecting rows with Age missing (null)
print("\nRows with missing Age:")
print(df[df['Age'].isnull()])

# 2. Data Cleaning and Preprocessing
# Dropping rows with missing values
cleaned_df = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(cleaned_df)

# 3. Data Aggregation and Grouping
# Computing average Age by City
agg_df = df.groupby('City')['Age'].mean().reset_index()
print("\nAverage Age by City:")
print(agg_df)

# 4. Data Transformation and Reshaping
# Transforming Age column to a categorical variable
df['Age Group'] = pd.cut(df['Age'], bins=[0, 30, 40, float('inf')], labels=['Young', 'Middle-aged', 'Old'])
print("\nDataFrame with Age Group column:")
print(df)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Selecting rows with Name starting with 'A'
print("\nRows with Name starting with 'A':")
print(df[df['Name'].str.startswith('A')])

# 2. Data Cleaning and Preprocessing
# Handling missing values by filling with a default value
df['Age'] = df['Age'].fillna(0)
print("\nDataFrame after handling missing values:")
print(df)


# 1. Advanced Filtering Techniques
# Filtering rows with Age greater than 30 and City containing 'York'
filtered_df = df[(df['Age'] > 30) & (df['City'].str.contains('York'))]
print("\nFiltered DataFrame (Age > 30 and City contains 'York'):")
print(filtered_df)

# 2. String Operations for Filtering
# Filtering rows with Name starting with 'A' or ending with 'e'
string_filtered_df = df[df['Name'].str.startswith('A') | df['Name'].str.endswith('e')]
print("\nFiltered DataFrame (Name starts with 'A' or ends with 'e'):")
print(string_filtered_df)

# 3. Indexing and Slicing
# Selecting rows and columns using loc[] and iloc[]
print("\nSelecting rows and columns using loc[]:")
print(df.loc[df['Age'] > 30, ['Name', 'City']])

print("\nSelecting rows and columns using iloc[]:")
print(df.iloc[[1, 3], [0, 2]])

# 4. Advanced Selection Techniques
# Selecting a scalar value using at[] and iat[]
print("\nSelecting a scalar value using at[]:")
print(df.at[2, 'Age'])  # Selecting Age value at row index 2

print("\nSelecting a scalar value using iat[]:")
print(df.iat[3, 1])  # Selecting Age value at row index 3

