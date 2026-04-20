import numpy as np

arr = np.array([1, 2, 3, 4, 5])
greater_than = arr[arr > 3]
less_than = arr[arr < 4]

print("Matrix:", arr)
print("Greater than 3:", greater_than)
print("Less than 4:", less_than)