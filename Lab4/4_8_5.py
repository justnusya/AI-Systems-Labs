import numpy as np
import matplotlib.pyplot as plt

# 1. Параметри
K = 20
L = 0
N = 5

x = np.random.randint(L, N, size=K)

# 3. Нормалізація за формулою: (x - x_min) / (x_max - x_min)
x_min = x.min()
x_max = x.max()
x_normalized = (x - x_min) / (x_max - x_min)

# 4. Побудова графіків поруч
plt.figure(figsize=(12, 5))

# Графік 1: Початковий масив
plt.subplot(1, 2, 1) # 1 рядок, 2 стовпці, графік №1
plt.bar(range(K), x, color='blue')
plt.title(f"Початковий масив (від {L} до {N})")
plt.xlabel("Індекс")
plt.ylabel("Значення")

# Графік 2: Нормалізований масив
plt.subplot(1, 2, 2) # 1 рядок, 2 стовпці, графік №2
plt.bar(range(K), x_normalized, color='pink')
plt.title("Нормалізований масив (від 0 до 1)")
plt.xlabel("Індекс")
plt.ylabel("Нормалізоване значення")

plt.tight_layout()
plt.show()