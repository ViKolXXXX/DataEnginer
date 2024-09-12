import numpy as np

def f(x):
    return x**2 - 14*x + 1

# Определяем отрезок вокруг точки минимума
critical_point = 7
epsilon = 2  # Ширина отрезка

# Определяем границы отрезка
a = critical_point - epsilon
b = critical_point + epsilon

# Вычисляем значения функции в границах отрезка
f_a = f(a)
f_b = f(b)
f_critical = f(critical_point)

print(f"Отрезок: [{a}, {b}]")
print(f"f({a}) = {f_a}")
print(f"f({critical_point}) = {f_critical}")
print(f"f({b}) = {f_b}")

# Выводим результаты
min_value = min(f_a, f_critical, f_b)
print(f"Минимальное значение на отрезке: {min_value}")