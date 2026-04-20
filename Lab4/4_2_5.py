import importlib
import numpy as np

module_4_1_5 = importlib.import_module("4_1_5")
a = module_4_1_5.a

top_left = [0, 1]
bottom_right = [1, 2]

submatrix = a[top_left[0] : bottom_right[0] + 1, 
              top_left[1] : bottom_right[1] + 1]

print("Matrix:\n", a)
print("\nSubmatrix:\n", submatrix)