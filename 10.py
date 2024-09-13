def find_minimum(x0, step, epsilon):
    def f(x):
        return x ** 2 - 14 * x + 1

    # Этап 1: Нахождение отрезка, содержащего минимум
    max_iterations = 100
    k = 0  # Начальное значение итераций
    a, b = None, None

    while k < max_iterations:
        fx0 = f(x0)
        x1 = x0 + step
        fx1 = f(x1)

        if fx1 < fx0:
            x0 = x1
        else:
            step = -step
            x1 = x0 + step
            fx1 = f(x1)
            if fx1 < fx0:
                x0 = x1
            else:
                step /= 2

        if abs(step) < 1e-5:
            a = x0 - step
            b = x0 + step
            break

        k += 1

        if k == 3 and fx1 == fx0:
            a = x0 - step
            b = x0 + step
            break

    # Этап 2 и 3: Нахождение точки минимума методом деления по полам
    k = 0
    results = []
    step = 1

    while (b - a) / 2.0 > epsilon and k < 10:
        x1 = (a + b - step) / 2.0
        x2 = (a + b + step) / 2.0
        fx1 = f(x1)
        fx2 = f(x2)

        results.append((k, a, b, x1, x2, fx1, fx2, (b - a) / 2))

        if fx1 < fx2:
            b = x2
        elif fx1 > fx2:
            a = x1
        else:
            a = x1
            b = x2

        k += 1

    min_x = (a + b) / 2.0
    min_fx = f(min_x)

    print(f"Найденный отрезок, содержащий минимум: [{a}, {b}]")
    print(f"Точка минимума: {min_x:.10f}")
    print(f"Значение функции в точке минимума: {min_fx:.10f}")
    print("\nТаблица результатов:")
    print("k\t\ta\t\tb\t\tx1\t\tx2\t\tf(x1)\t\tf(x2)\t\t(b-a)/2")
    for row in results:
        print(
            f"{row[0]}\t\t{row[1]:.6f}\t{row[2]:.6f}\t{row[3]:.6f}\t{row[4]:.6f}\t{row[5]:.6f}\t{row[6]:.6f}\t{row[7]:.6f}")

# Начальные параметры
x0 = 0
step = 1.0
epsilon = 0.1

# Нахождение минимума функции
find_minimum(x0, step, epsilon)
