import numpy as np
import pandas as pd


def f(x):
    """Функция для нахождения минимума."""
    return x ** 2 + (-1) * x * 14 + 1


def find_minimum():
    # Инициализация
    k = 0 #Это счетчик итераций. Он будет увеличиваться каждый раз, когда мы находим новое значение, в которое движемся.
    x0 = np.random.randint(-10, 10)  # Сначала выбираем начальное значение x0 произвольно. Это значение, с которого начинается поиск минимума.
    step = 1.0  # Определяем величину шага
    a, b = None, None

    # Поиск направления убывания
    while True:
        f_x0 = f(x0) #Вычисляем значение функции f(x0). Это значение будет использоваться для сравнения в последующих шагах.
        print(k, x0, f_x0)

        # Проверка на уменьшение
        x1 = x0 + step #Вычисляем новую точку
        f_x1 = f(x1) #Вычисляем значение функции в новой точке.

        if f_x1 < f_x0:
            #Это значит, что мы нашли точку, где значение функции меньше, чем в x0. В этом случае
            x0 = x1  # Двигаемся вправо
            k += 1
        else:
            #Значит, значение функции увеличилось, и нам нужно изменить направление.
            step = -step  # Меняем направление, т.е., теперь будем двигаться влево (уменьшая x).
            x1 = x0 + step
            f_x1 = f(x1)

            if f_x1 < f_x0:
                x0 = x1  # Двигаемся влево
                k += 1
            else:
                step /= 2  # Уменьшаем шаг
                if k >= 3 and f_x1 == f_x0:
                    a, b = x0 - step, x0 + step  # Определяем отрезок
                    break

    # Удвоение шага
    step *= 2
    x_k_plus_1 = x0 + step

    # Определение точки возрастания
    while True:
        f_x_k_plus_1 = f(x_k_plus_1)

        if f_x_k_plus_1 < f(x0):
            x0 = x_k_plus_1  # Двигаемся вправо
            k += 1
            x_k_plus_1 = x0 + step
        else:
            a, b = (x0 - step, x_k_plus_1) if x_k_plus_1 > x0 else (x_k_plus_1, x0)
            break
    print(a, b)
    # Метод деления функции пополам
    e = 0.1  # Точность
    results = []

    while (b - a) / 2 > e:  # Проверка на точность
        x1 = (a + b - step) / 2
        x2 = (a + b + step) / 2
        f_x1 = f(x1)
        f_x2 = f(x2)

        # Сохранение результатов для таблицы
        results.append([k, a, b, x1, x2, f_x1, f_x2, (b - a) / 2])

        if f_x1 < f_x2:
            b = x2  # Уменьшаем верхнюю границу
        else:
            a = x1  # Увеличиваем нижнюю границу

    # Вывод результатов
    min_x = (a + b) / 2
    min_f = f(min_x)

    # Конвертация результатов в DataFrame и вывод
    df = pd.DataFrame(results, columns=["k", "a", "b", "x1", "x2", "f(x1)", "f(x2)", "(b-a)/2"])
    print(df)
    print(f"Минимум функции достигается в x = {min_x}, f(x) = {min_f}")


if __name__ == "__main__":
    find_minimum()