import numpy as np

angle = np.pi / 4  # 45 degrees in radians
print("Sin of angle:", np.sin(angle))  # Output: 0.7071067811865476
print("Cos of angle:", np.cos(angle))  # Output: 0.7071067811865476
print("Tan of angle:", np.tan(angle))  # Output: 0.9999999999999999

arr = np.array([1, 2, 3])
print("Exponential of array elements:", np.exp(arr))  # Output: [ 2.71828183  7.3890561  20.08553692]

arr = np.array([1, 10, 100])
print("Natural logarithm:", np.log(arr))  # Output: [0.  2.30258509 4.60517019]
print("Base-10 logarithm:", np.log10(arr))  # Output: [0. 1. 2.]
print("Base-2 logarithm:", np.log2(arr))  # Output: [0.         3.32192809 6.64385619]


arr = np.array([[1, 2], [3, 4]])
print("Sum of array elements:", np.sum(arr))  # Output: 10

arr = np.array([[1, 2], [3, 4]])
print("Mean of array elements:", np.mean(arr))  # Output: 2.5 " Avarage of 1 and 2 is 1.5 and from 3,4 
                                                    # is 3.5. The sum is then halved by thenumber of arrays."

arr = np.array([[1, 2], [3, 4]])
print("Maximum element:", np.max(arr))  # Output: 4
print("Minimum element:", np.min(arr))  # Output: 1

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.reshape(arr, (2, 3))
print("Reshaped array:")
print(reshaped_arr) # Output: [[1 2 3]
                              #[4 5 6]]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print("Concatenated array:")
print(concatenated_arr) # Output:[[1 2]
                                # [3 4]
                                # [5 6]]