import numpy as np

arr = np.array([1, 2, 3, 4, 5])
condition = arr > 2
result = arr[condition]
print("Elements greater than 2:", result)  # Output: [3 4 5]

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices]
print("Elements at indices 0, 2, and 4:", result)  # Output: [1 3 5]

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
slice_result = arr[:2, 1:]  # Selects rows 0 and 1, and columns 1 and 2
print("Sliced Array:")
print(slice_result)