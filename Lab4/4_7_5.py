import numpy as np

k = 7
variant = 5
matrix = np.zeros((k, k), dtype=int)

matrix[0::2, 1::2] = variant
matrix[1::2, 0::2] = variant

print(f"Матриця {k}x{k} для варіанту {variant}:")
print(matrix)