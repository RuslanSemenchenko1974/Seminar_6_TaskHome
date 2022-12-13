"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и
чего удалось добиться"""

"""Задача 5 доп., 3 семинар

Составьте список чисел Фибоначчи - Вычисление с помощью цикла for """

"""Улучшить выделение памяти не удалось, Вычисление с помощью цикла for и 
рекурсии требует примерно одинаковый объем памяти"""

from memory_profiler import profile

@profile
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

    for i in range(22):
        print(f'{i + 1} = {fibonacci_for(i + 1)}')

culc_f_for()