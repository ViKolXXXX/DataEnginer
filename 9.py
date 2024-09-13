import math
import numpy as np

# Определение функции f(x)
def f(x):
    return x ** 2 + (-1) * x * 14 + 1

# Начальные значения
x0 = np.random.randint(-10, 10)
step = 1
e = 0.1

# Этап 1: Нахождение начального интервала
k = 0
while True:
    fx0 = f(x0)
    x1 = x0 + step
    fx1 = f(x1)

    if fx1 < fx0:
        a, b = x0, x1
        break

    step = -step
    x1 = x0 + step
    fx1 = f(x1)

    if fx1 < fx0:
        a, b = x0, x1
        break

    step /= 2
    k += 1

    if k >= 3 and math.isclose(fx1, fx0):
        a, b = x0 - step, x0 + step
        break

print(f"Начальный интервал: [{a}, {b}]")
print(f"Количество итераций для нахождения интервала: {k}")

# Этап 2 и 3: Нахождение минимума методом деления отрезка пополам
k = 0
step = (b - a) / 4

print("\nk\ta\tb\tx1\tx2\tf(x1)\tf(x2)\t(b-a)/2")

while (b - a) / 2 > e and k < 10:
    x1 = (a + b - step) / 2
    x2 = (a + b + step) / 2
    fx1 = f(x1)
    fx2 = f(x2)

    print(f"{k}\t{a:.4f}\t{b:.4f}\t{x1:.4f}\t{x2:.4f}\t{fx1:.4f}\t{fx2:.4f}\t{(b - a) / 2:.4f}")

    if fx1 < fx2:
        b = x2
    elif fx1 > fx2:
        a = x1
    else:
        a, b = x1, x2

    k += 1

# Вычисление окончательного результата
minx = (a + b) / 2
miny = f(minx)

print(f"\nМинимум функции:")
print(f"x = {minx:.4f}")
print(f"f(x) = {miny:.4f}")
