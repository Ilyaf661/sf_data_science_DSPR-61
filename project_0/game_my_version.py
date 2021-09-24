# Создание случайного числа от 1 до 100.
import numpy as np


# Функция бинарного поиска.
def binary_search(number):
    predict = list(range(1, 101))  # Список чисел от 1 до 100.
    first = 1  # Нижний предел списка.
    last = 100  # Верхний предел списка.
    index = 0  # Переменная для хранения индекса искомого числа.
    count = 0  # Счетчик попыток.
    while (first <= last) and (index == 0):
        count += 1
        mid = (first + last) // 2  # Находим среднее значение.
        # Если индекс числа mid в списке predict == загаданному числу.
        if predict[mid] == number:
            index = mid  # Присваиваем его значение переменной индекс.
        else:
            # Если загаданное число меньше predict[mid].
            if number < predict[mid]:
                last = mid - 1  # Ищем в левой стороне списка predict.
            else:
                # Иначе ищем в правой стороне списка predict.
                first = mid + 1
    # Для просмотра найденного значения введи print(index+1).
    return count  # Возращаем значение счетчика попыток.


# Функция по запуску первой функции 1000 раз.
def score_game(binary_srch):
    # Создаем список, в котором будут храниться ответы.
    count_ls = []
    # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    # Создаем 1000 случайных чисел от 1 до 100.
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        # Добавляем в список все полученные ответы.
        count_ls.append(binary_srch(number))
    # Находим средне-арифметическое попыток.
    score = round(float(np.mean(count_ls)))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")


score_game(binary_search)  # Запускаем функцию.