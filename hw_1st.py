__author__ = 'Мишин Егор Олегович'

'''
Проанализировать скорость и сложность одного - трёх любых алгоритмов, 
разработанных в рамках домашнего задания первых трех уроков.
'''

'''
Условие задачи:
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''
'''
В домашнем задании 2го урока решил эту задачу через рекурсию. Следом добавлю решение без нее.
'''

import cProfile
import functools
import sys


def sum_el(n, num=1):
    if n == 1:
        return num

    if n > 900:
        return 0.666666666666

    if n > 1:
        return num + sum_el(n - 1, num / (-2))


# lenth = int(input('Введите число элементов: '))
# print(f'сумма = {sum_el(lenth)}')

# timeit: python -m timeit -n 100 -s "import hw_1st" "hw_1st.sum_el(100)"
# 100 loops, best of 5: 42.6 usec per loop      <- 100
# 100 loops, best of 5: 117 usec per loop       <- 400


# cProfile.run(f'sum_el(lenth)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 100/1    0.000    0.000    0.000    0.000     hw_2nd.py:22(sum_el)    <- 100
# 400/1    0.000    0.000    0.000    0.000     hw_2nd.py:22(sum_el)    <- 400


'''
p.s. Для нагляности я вручную отодвинул последний столбец
'''

'''
Второй вариант решения
'''

# n = int(input('Сколько элементов сложить: '))


def sum_el_2(n):
    item = 1
    summa = 0
    for _ in range(n):
        summa += item
        item /= -2
    # print(summa)

# timeit: python -m timeit -n 100 -s "import hw_1st" "hw_1st.sum_el_2(100)"
# 100 loops, best of 5: 156 usec per loop       <- 100
# 100 loops, best of 5: 68.4 usec per loop      <- 400


# cProfile.run(f'sum_el_2(n)')
# ncalls  tottime  percall  cumtime  percall  filename:lineno(function)
#   1    0.000    0.000    0.000    0.000       hw_2nd.py:54(sum_el_2)    <- 10
#   1    0.000    0.000    0.000    0.000       hw_2nd.py:54(sum_el_2)    <- 400


'''
3-ий вариант
'''


def sum_el_3(n):
    summa_2 = 2 * (1 - (-0.5) ** n) / 3
    # print(summa_2)


# timeit: python -m timeit -n 100 -s "import hw_1st" "hw_1st.sum_el_3(100)"
# 100 loops, best of 5: 905 nsec per loop      <- 100
# 100 loops, best of 5: 535 nsec per loop      <- 400


# cProfile.run(f'sum_el_3(n)')
# ncalls  tottime  percall  cumtime  percall   filename:lineno(function)
#   1    0.000    0.000    0.000    0.000       hw_2nd.py:63(sum_el_3)    <- 10
#   1    0.000    0.000    0.000    0.000       hw_2nd.py:63(sum_el_3)    <- 400

