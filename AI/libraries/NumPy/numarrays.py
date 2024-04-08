import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1d)

# Create a 2D array from a nested Python list
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr2d)

print("First element of arr1d:", arr1d[0])
print("Last element of arr1d:", arr1d[-1])

# Accessing elements of a 2D array
print("\nElement at row 1, column 2 of arr2d:", arr2d[0, 1])

# Slicing arrays
print("\nSlice of arr1d:", arr1d[1:4])
print("Slice of arr2d:")
print(arr2d[1:, :2])

# Element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Sum of arrays:", arr1 + arr2)
print("Product of arrays:", arr1 * arr2)

# Broadcasting
scalar = 10
print("\nAdding scalar to array:", arr1 + scalar)
arr1d = np.array([1, 2, 3, 4, 5])
# Square root
print("Square root:", np.sqrt(arr1d))  # output: [1,1.41421356 , 1.73205081, 2 , 2.23606798]

# Exponential
print("Exponential:", np.exp(arr1d))  # output: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]

# Sum of array elements
print("Sum of array elements:", np.sum(arr1d))  # Output: 15

# Mean of array elements
print("Avarage of array elements:", np.mean(arr1d))  # Output: 3.0

# Maximum element
print("Maximum element:", np.max(arr1d))  # Output: 5

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

# Element-wise comparison
print("Element-wise comparison result:", arr1 == arr2)  # Output: [False  True False]