import numpy as np

# Example 1: Element-wise Exponential
arr = np.array([1, 2, 3, 4, 5])
result_exp = np.exp(arr)

# Example 2: Element-wise Square Root
result_sqrt = np.sqrt(arr)

# Example 3: Element-wise Logarithm (Natural Logarithm)
result_log = np.log(arr)

# Example 4: Element-wise Sine
angles_rad = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
result_sin = np.sin(angles_rad)

# Example 5: Element-wise Comparison
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 3, 3, 4, 4])
result_comparison = arr1 > arr2

# Example 6: Broadcasting with Scalar
arr_scalar = np.array([1, 2, 3, 4, 5])
result_broadcasting_scalar = arr_scalar + 10

print("Original Array:", arr)
print("Element-wise Exponential Result:", result_exp)
print("Element-wise Square Root Result:", result_sqrt)
print("Element-wise Logarithm Result:", result_log)
print("Element-wise Sine Result:", result_sin)
print("Element-wise Comparison Result:", result_comparison)
print("Broadcasting with Scalar Result:", result_broadcasting_scalar)
