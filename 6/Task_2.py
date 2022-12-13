"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться"""

"""Напишите программу, которая будет преобразовывать десятичное число в
двоичное."""

"""Первый способ решение через строку, второй через список, требуется примерно
 одинаковое количество памяти"""

from memory_profiler import profile


@profile
def function_1():
    while True:
        try:
            us_namber = int(input("Введите число : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            break

    binary_number = ''
    while us_namber > 1:
        temp = us_namber % 2
        binary_number = str(temp) + binary_number
        us_namber = us_namber // 2
        if us_namber == 1:
            binary_number = "1" + binary_number
    print(f"Число  в двоичной системе : {binary_number}")


@profile
def function_2():
    while True:
        try:
            us_namber = int(input("Введите число : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            break

    binary_number = []
    while us_namber > 1:
        temp = us_namber % 2
        binary_number.append(temp)
        us_namber = us_namber // 2
        if us_namber == 1:
            binary_number.append(1)
    binary_number.reverse()
    print(f"Число в двоичной системе : {binary_number}")


function_2()
function_1()
