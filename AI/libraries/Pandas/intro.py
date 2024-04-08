import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, 7, 9])
print("Series:")
print(s)

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Boston']}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Accessing elements in a Series
print("\nAccessing elements in Series:")
print("First element of the Series:", s[0])
print("Last element of the Series:", s[len(s)-1])  # Alternatively, you can use s[-1]

# Accessing columns in a DataFrame
print("\nAccessing columns in DataFrame:")
print("Name column:")
print(df['Name'])
print("\nAge column:")
print(df['Age'])

# Accessing rows in a DataFrame
print("\nAccessing rows in DataFrame:")
print("First row of the DataFrame:")
print(df.iloc[0])  # Using iloc to access rows by integer index
print("\nLast row of the DataFrame:")
print(df.iloc[-1])

# Getting information about the DataFrame
print("\nInformation about the DataFrame:")
print(df.info())

# Summary statistics of the DataFrame
print("\nSummary statistics of the DataFrame:")
print(df.describe())

