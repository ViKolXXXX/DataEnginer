def f(x):
    return x ** 2 - 14 * x + 1


def bisection_min(a, b, epsilon):
    while (b - a) / 2.0 > epsilon:
        print("итерация")
        midpoint = (a + b) / 2.0
        left = midpoint - epsilon
        right = midpoint + epsilon

        if f(left) < f(right):
            b = right
        else:
            a = left

    return (a + b) / 2.0


# Пример использования
a = -4.0
b = 12
epsilon = 0.1

minimum = bisection_min(a, b, epsilon)
print(f"Точка минимума: {minimum}")
print(f"Значение функции в точке минимума: {f(minimum)}")