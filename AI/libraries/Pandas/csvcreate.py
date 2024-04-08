import csv

# Sample data
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago'],
    ['David', 40, 'Houston'],
    ['Eve', 45, 'Boston']
]

# File path for the CSV file
file_path = 'sample_data.csv'

# Writing data to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_path}' created successfully.")
