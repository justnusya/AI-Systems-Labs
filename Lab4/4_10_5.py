import numpy as np
import matplotlib.pyplot as plt

# Визначаємо проміжок, щоб захопити обидві частини (x < 1 та x > 10)
x = np.linspace(-2, 12, 1000)

# Частина 1: ln(sin(x) + 0.5)
# Використовуємо np.log для натурального логарифма
y1 = np.log(np.sin(x) + 0.5)

# Частина 2: ctg(x^2) / sqrt(1 - arcsin(x))
# ctg = 1 / tan
# arcsin(x) визначений лише від -1 до 1, умова x > 10.
y2 = (1 / np.tan(x**2)) / np.sqrt(1 - np.arcsin(x))

# 3. Об'єднуємо за допомогою np.select (це зручніше для 3-х станів: умова1, умова2 і все інше)
conditions = [
    (x < 1),
    (x > 10)
]
choices = [y1, y2]

# Там, де умови не виконуються, буде np.nan (графік просто перерветься)
y = np.select(conditions, choices, default=np.nan)

# 4. Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y(x)', color='red', linewidth=2)

# Оформлення
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.title("Графік складної функції (Варіант 5)")
plt.xlabel("x")
plt.ylabel("y")

# Обмежимо Y, бо тангенс і логарифм можуть "летіти" в нескінченність
plt.ylim(-5, 5) 
plt.xlim(-5, 25) 

plt.legend()
plt.show()