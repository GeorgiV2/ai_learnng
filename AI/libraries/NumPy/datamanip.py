import numpy as np

# Create sample data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Save data to a CSV file
np.savetxt(r'C:\Users\Admin\Desktop\programing stuff\Projects\AI\libraries\NumPy\data.csv', data, delimiter=',')

# Load data from a text file
loaded_data = np.loadtxt(r'C:\Users\Admin\Desktop\programing stuff\Projects\AI\libraries\NumPy\data.txt', delimiter=',')


# Normalize loaded data
normalized_data = (loaded_data - np.mean(loaded_data)) / np.std(loaded_data)

# Standardize loaded data
standardized_data = (loaded_data - np.min(loaded_data)) / (np.max(loaded_data) - np.min(loaded_data))

# Save loaded data to a different file
np.savetxt('data_out.txt',standardized_data, delimiter=',')