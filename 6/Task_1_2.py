"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться.

Напишите программу, которая принимает на вход вещественное
число и показывает сумму его цифр

Используется два метода : математический и с помощью функций str

Оба варианта примерно одинаковые"""

from timeit import timeit


def function_math():
    namber = 88888.88888
    if int(namber) < namber:
        while int(namber) != namber:
            namber *= 10
    namber = int(namber)

    temp = 0
    while namber > 0:
        temp = temp + namber % 10
        namber = namber // 10
    # print(f'Сумма цыфр : {temp}')


def function_string():
    namber = 88888.88888
    namber = str(namber)
    namber = namber.split(".")
    namber = namber[0] + namber[1]
    summ_n = 0
    for i in namber:
        summ_n += int(i)
    # print(f'Сумма цыфр : {summ_n}')


# function_math()
# function_string()
print(timeit("function_math()", "from __main__ import function_math",
             number=10000))
print(timeit("function_string()", "from __main__ import function_string",
             number=10000))
