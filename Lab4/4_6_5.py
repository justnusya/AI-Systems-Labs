import numpy as np

k = 7
variant = 5
matrix = np.zeros((k, k), dtype=int)
center = k // 2

for i in range(k):
    for j in range(k):
        if abs(i - center) + abs(j - center) == center:
            matrix[i, j] = variant

print(f"Матриця {k}x{k} для варіанту {variant}:")
print(matrix)