
import math


def f(x):
    return x ** 2 + (-1) * x * 14 + 1

def golden_section_search(a, b, epsilon):
    phi = (1 + math.sqrt(5)) / 2  # Золотое сечение
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    while abs(b - a) > epsilon:
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

    return (a + b) / 2


# Задаем начальные параметры
a = 10
b =
epsilon = 0.1

# Вызываем функцию для поиска точки минимума
minimum_point = golden_section_search(a, b, epsilon)

# Выводим результат
print("Точка минимума функции:", minimum_point)
print("Значение функции в точке минимума:", f(minimum_point))