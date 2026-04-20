import numpy as np

K, L = 10, 10  # Розмір матриці
# 1. Створюємо матрицю випадкових чисел від 0 до 255
matrix = np.random.randint(0, 256, (K, L))

# 2. Створюємо копію для результату (щоб не змінювати оригінал під час обчислень)
# Використовуємо .astype(float), щоб при діленні не втрачати точність
result = matrix.copy().astype(float)

# 3. Вибираємо всі 8 сусідів та центральний елемент (зрізи)
# Внутрішні елементи - це [1:-1, 1:-1]
top_left     = matrix[0:-2, 0:-2]
top_center   = matrix[0:-2, 1:-1]
top_right    = matrix[0:-2, 2:]
mid_left     = matrix[1:-1, 0:-2]
center       = matrix[1:-1, 1:-1] # Сам елемент
mid_right    = matrix[1:-1, 2:]
bot_left     = matrix[2:,   0:-2]
bot_center   = matrix[2:,   1:-1]
bot_right    = matrix[2:,   2:]

# 4. Обчислюємо середнє арифметичне без циклів
smoothed = (top_left + top_center + top_right + 
            mid_left + center     + mid_right + 
            bot_left + bot_center + bot_right) / 9

# 5. Записуємо результат у внутрішню частину
result[1:-1, 1:-1] = smoothed

print("Оригінальна матриця (фрагмент):\n", matrix[:5, :5])
print("\nЗгладжена матриця (фрагмент):\n", result[:5, :5].astype(int))