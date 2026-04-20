import numpy as np

k = 4
variant = 5
matrix = np.zeros((k, k), dtype=int)
np.fill_diagonal(np.fliplr(matrix), variant)

print(f"Матриця {k}x{k} з варіантом {variant} на побічній діагоналі:")
print(matrix)