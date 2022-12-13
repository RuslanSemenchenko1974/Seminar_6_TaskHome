"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться.

Задача №5 к 4 семинару:

Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат вычисления произведения всех
элементов списка.

Второй вариант функция c_test2, через for без генератора и не через функцию
append, список чисел для удобства от 100 до 200"""

from timeit import timeit
from functools import reduce


def c_test1():
    generator = (i for i in range(100, 201) if i % 2 == 0)
    my_lst = []
    for el in generator:
        my_lst.append(el)
    mult_all = reduce(lambda x, y: x * y, my_lst)
    # print(my_lst)
    # print(mult_all)
    return mult_all


def c_test2():
    my_lst = []
    mult_all = 1
    for el in range(100, 201):
        if el % 2 == 0:
            mult_all *= el
            my_lst += [el]
    # print(my_lst)
    # print(mult_all)
    return mult_all


print(timeit("c_test1()", "from __main__ import c_test1", number=100))

print(timeit("c_test2()", "from __main__ import c_test2", number=100))

# c_test1()
# c_test2()
"""Второй вариант быстрее примерно на 25%-30%"""
