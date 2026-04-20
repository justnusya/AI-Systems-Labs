import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr_indices = np.array([0, 2, 4]) 

result = arr[arr_indices]

print("Matrix:", arr)
print("Searching indices:", arr_indices)
print("Result:", result)
