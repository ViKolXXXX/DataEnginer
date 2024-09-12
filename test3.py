import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Определение целевой функции
def f(x):
    """Целевая функция для нахождения минимума."""
    return x ** 2 - 14 * x + 1


# Функция для нахождения минимума
def find_minimum():
    # Этап 1: Инициализация
    k = 0  # Счетчик итераций
    x0 = np.random.uniform(-10, 10)  # Случайное начальное значение x
    step = 1.0  # Начальный шаг для изменения x
    results = []  # Список для хранения результатов итераций

    while True:
        f_x0 = f(x0)  # Находим значение функции в текущей точке x0

        # Находим новую точку на основе текущего шага
        x1 = x0 + step
        f_x1 = f(x1)  # Вычисляем значение функции в новой точке x1

        # Проверка, уменьшилось ли значение функции
        if f_x1 < f_x0:
            # Если значение функции уменьшилось, переходим вправо
            x0 = x1  # Обновляем x0
            k += 1  # Увеличиваем счетчик итераций
        else:
            # Если значение функции увеличилось, изменяем направление
            step = -step  # Меняем направление шага
            x1 = x0 + step  # Вычисляем новую точку с измененным направлением
            f_x1 = f(x1)  # Вычисляем значение функции в новой точке x1

            # Проверяем, уменьшилось ли значение функции после изменения направления
            if f_x1 < f_x0:
                x0 = x1  # Обновляем x0
                k += 1  # Увеличиваем счетчик итераций
            else:
                # Если значение не уменьшилось, уменьшаем шаг
                step /= 2
                # Проверяем, если после 3 итераций значение не изменилось
                if k >= 3 and f_x1 == f_x0:
                    # Если не было изменений, определяем отрезок [a, b] для последующего поиска минимума
                    a, b = x0 - step, x0 + step
                    print(a, b)
                    break  # Выходим из цикла

    # Этап 2: Метод деления функции пополам
    results = []  # Список для хранения результатов
    e = 0.1  # Задаем точность

    while (b - a) / 2 > e:  # Проверка на точность
        # Находим середину отрезка для деления
        x1 = (a + b - step) / 2
        x2 = (a + b + step) / 2
        f_x1 = f(x1)  # Вычисляем значение функции в x1
        f_x2 = f(x2)  # Вычисляем значение функции в x2

        # Сохраняем результаты для таблицы
        results.append([k, a, b, x1, x2, f_x1, f_x2, (b - a) / 2])

        # Сравниваем значения функции в x1 и x2 для определения нового отрезка
        if f_x1 < f_x2:
            b = x2  # Уменьшаем верхнюю границу отрезка
        else:
            a = x1  # Увеличиваем нижнюю границу отрезка

    # Вычисляем минимум
    min_x = (a + b) / 2  # Находим середину отрезка
    min_f = f(min_x)  # Вычисляем значение функции в минимальной точке

    # Конвертация результатов в DataFrame и вывод
    df = pd.DataFrame(results, columns=["k", "a", "b", "x1", "x2", "f(x1)", "f(x2)", "(b-a)/2"])
    print(results)
    print(df)  # Выводим таблицу результатов
    print(f"Минимум функции достигается в x = {min_x}, f(x) = {min_f}")  # Выводим найденный минимум

    # Визуализация функции
    x_vals = np.linspace(min_x - 5, min_x + 5, 100)  # Создаем массив значений для графика
    y_vals = [f(x) for x in x_vals]  # Вычисляем значения функции для графика

    plt.plot(x_vals, y_vals, label='f(x) = x^2 - 14x + 1')  # Строим график функции
    plt.scatter([min_x], [min_f], color='red', label='Минимум', zorder=5)  # Отмечаем минимум
    plt.title('График функции')  # Заголовок графика
    plt.xlabel('x')  # Подпись оси X
    plt.ylabel('f(x)')  # Подпись оси Y
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Горизонтальная линия на уровне 0
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Вертикальная линия на уровне 0
    plt.legend()  # Легенда графика
    plt.grid()  # Сетка на графике
    plt.show()  # Отображаем график


if __name__ == "__main__":
    find_minimum()  # Запускаем функцию поиска минимума