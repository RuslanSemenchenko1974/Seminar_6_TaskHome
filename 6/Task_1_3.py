"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться.

Задача 5 доп., 3 семинар

Составьте список чисел Фибоначчи

Используется два метода: рекурсии и с помощью цикла for

При больших числах гораздо быстрее вычисление с помощьюцикла for!"""

from timeit import timeit


def culc_f_rec():
    def fibonacci(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(30):
        # print(f'{i + 1} = {fibonacci(i + 1)}')
        f_prom = fibonacci(i + 1)


def culc_f_for():
    def fibonacci_for(n_f):
        l_feb = [0, 1, 1]
        if n_f == 1:
            return 1
        elif n_f == 2:
            return 1
        else:
            for j in range(3, n_f + 1):
                prom = l_feb[j - 1] + l_feb[j - 2]
                l_feb.append(prom)
            return l_feb[n_f]

    for i in range(30):
        # print(f'{i + 1} = {fibonacci_for(i + 1)}')
        f_prom = fibonacci_for(i + 1)


print(timeit("culc_f_rec()", "from __main__ import culc_f_rec", number=10))
print(timeit("culc_f_for()", "from __main__ import culc_f_for", number=10))
