
# NumPy Assignment Solutions

import numpy as np

# 1. Create a 3x3 Identity Matrix with Float Data Type
identity_matrix = np.eye(3, dtype=float)
print("1. Identity Matrix:\n", identity_matrix)

# 2. Create a 1D Array with Random Values Between 0 and 1
random_array = np.random.rand(10)  # Adjust size as needed
print("\n2. 1D Random Array:\n", random_array)

# 3. Create a 2D Array with Random Integer Values
random_2d_array = np.random.randint(0, 100, size=(3, 3))  # Specify range and size
print("\n3. 2D Random Integer Array:\n", random_2d_array)

# 4. Create an Array Using a Custom Function
def custom_function(x):
    return x**2
custom_array = np.fromfunction(lambda i, j: custom_function(i + j), (3, 3), dtype=int)
print("\n4. Custom Function Array:\n", custom_array)

# 5. Reshape a 1D Array into a 2D Array
one_d_array = np.arange(12)
reshaped_array = one_d_array.reshape(3, 4)
print("\n5. Reshaped Array:\n", reshaped_array)

# 6. Create a 3x3 Array of Ones
ones_array = np.ones((3, 3))
print("\n6. Array of Ones:\n", ones_array)

# 7. Get Common Items Between Two Arrays
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
common_items = np.intersect1d(a, b)
print("\n7. Common Items:\n", common_items)

# 8. Remove Items from Array `a` Present in Array `b`
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
result = np.setdiff1d(a, b)
print("\n8. Array after Removal:\n", result)

# 9. Limit the Number of Items Printed in an Array
a = np.arange(15)
np.set_printoptions(threshold=6)
print("\n9. Limited Print Array:\n", a)

# 10. Drop NaN Values
array_with_nan = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
cleaned_array = array_with_nan[~np.isnan(array_with_nan)]
print("\n10. Array without NaN:\n", cleaned_array)

# 11. Create a 1D Array of First 20 Natural Numbers and a 2D Array
one_d_array = np.arange(1, 21)
two_d_array = one_d_array.reshape(4, 5)
print("\n11. 1D Array:\n", one_d_array)
print("11. 2D Array:\n", two_d_array)

# 12. Analyze a 3D Array's Properties and Change Data Type
three_d_array = np.random.randint(1, 10, size=(2, 3, 4))
print("\n12. 3D Array Properties:")
print("Shape:", three_d_array.shape)
print("Size:", three_d_array.size)
print("Dimensions:", three_d_array.ndim)
print("Data Type:", three_d_array.dtype)
float_array = three_d_array.astype(np.float64)
print("New Data Type:", float_array.dtype)

# 13. Reshape and Flatten an Array
original_array = np.arange(12)
reshaped_array = original_array.reshape(3, 4)
flattened_array = reshaped_array.ravel()
print("\n13. Flattened matches original:", np.array_equal(flattened_array, original_array))

# 14. Perform Element-Wise Operations and Explain Division by Zero
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\n14. Element-wise Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 15. Use Broadcasting in Addition
array_2d = np.array([[1], [2], [3]])
array_1d = np.array([4, 5, 6])
result = array_2d + array_1d
print("\n15. Broadcasting Result:\n", result)

# 16. Replace Elements Greater Than 5
random_array = np.random.randint(0, 10, size=(3, 3))
mask = random_array > 5
random_array[mask] = 5
print("\n16. Elements Replaced:\n", random_array)

# 17. Extract Rows, Columns, and Subarrays
array = np.random.randint(0, 10, size=(4, 4))
print("\n17. Row, Column, Subarray:")
print("Second Row:", array[1])
print("Last Column:", array[:, -1])
print("Subarray (First 2x2):", array[:2, :2])

# 18. Practical Example of NumPy in AI/ML/EDA
data = np.random.rand(100, 3)  # Example: Random data generation
print("\n18. Mean of Columns:", data.mean(axis=0))  # Useful in EDA

# 19. Compute Eigenvalues and Eigenvectors
matrix = np.random.rand(4, 4)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
reconstructed_matrix = eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)
print("\n19. Eigenvalues Reconstruction Matches:", np.allclose(matrix, reconstructed_matrix))

# 20. Reshape and Flatten a 3D Array
array_3d = np.arange(27).reshape(3, 3, 3)
flattened_array = array_3d.ravel()
print("\n20. Flattened matches original:", np.array_equal(flattened_array, np.arange(27)))

# 21. Compare `np.dot()` and `@`
array_a = np.random.rand(1000, 500)
array_b = np.random.rand(500, 1000)
result_dot = np.dot(array_a, array_b)
result_at = array_a @ array_b
print("\n21. Matrix Multiplication Completed")

# 22. Broadcasting with `np.newaxis`
array_3d = np.random.rand(2, 1, 4)
array_2d = np.random.rand(4, 1)
result = array_3d + array_2d.T  # With broadcasting
manual_result = array_3d + array_2d[:, np.newaxis]
print("\n22. Broadcasting Result:", result)

# 23. Replace Values Based on a Mask
random_floats = np.random.rand(4, 4)
mask = random_floats < 0.5
random_floats[mask] **= 2
print("\n23. Values Replaced:\n", random_floats)

# 24. Slicing Operations
array = np.arange(1, 26).reshape(5, 5)
print("\n24. Sliced Array Results:")
print("Diagonal:", np.diag(array))
array[2] = 0
print("Middle Row Zeroed:", array)
print("Flipped Vertically:", np.flipud(array))
print("Flipped Horizontally:", np.fliplr(array))

# 25. Advanced Slicing and Mean Along Axis
array_4d = np.random.randint(0, 100, size=(2, 3, 4, 5))
subarray = array_4d[:, :2, :, :3]
mean = subarray.mean(axis=1)
print("\n25. Subarray Mean:", mean)

# 26. Reshape Array and Discuss Impacts
array = np.arange(200).reshape(10, 20)
reshaped_20_10 = array.reshape(20, 10)
reshaped_5_40 = array.reshape(5, 40)
print("\n26. Reshaped Arrays Completed")

# 27. Large 2D Array Manipulations
large_array = np.arange(10000).reshape(100, 100)
reshaped = large_array.reshape(10, 1000)
print("\n27. Large Array Reshaping Completed")

# 28. Upper and Lower Triangular Operations
matrix = np.random.randint(1, 10, size=(6, 6))
upper_triangle = np.triu(matrix)
print("\n28. Upper Triangle:\n", upper_triangle)
