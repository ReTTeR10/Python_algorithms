__author__ = 'Мишин Егор Олегович'
'''
Python 3.6.5 (Anaconda)
Windows 10 Pro x64
'''
import sys
from random import randint

# Функция проверки


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)



# Для анализа использования памяти возьмем задачу 3го урока

'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

list_1 = [randint(1, 100) for _ in range(1, 20)]
maximum = list_1[0]
minimum = list_1[0]
max_index = 0
min_index = 0

print(f'Исходный список: {list_1}')
for i, item in enumerate(list_1):
    if item > maximum:
        maximum = item
        max_index = i
    if item < minimum:
        minimum = item
        min_index = i

print(f'\nmax = {maximum} max_index = {max_index}\n min = {minimum} min_index = {min_index}')
list_1[max_index], list_1[min_index] = list_1[min_index], list_1[max_index]
print(f'\nИзмененный список: {list_1}')

print('check_memory(list_1) \n *****')
show_size(list_1)
print('show_size(maximum) \n *****')
show_size(maximum)
print('show_size(minimum \n *****')
show_size(minimum)
print('show_size(max_index) \n *****')
show_size(max_index)
print('show_size(min_index) \n *****')
show_size(min_index)
print('getsizeof')



print('*'*100)
##########################################################################
'''Результаты'''
# Исходный список: [25, 23, 83, 92, 38, 60, 52, 44, 63, 69, 49, 86, 79, 37, 15, 82, 13, 23, 62]
#
# max = 92 max_index = 3
#  min = 13 min_index = 16
#
# Измененный список: [25, 23, 83, 13, 38, 60, 52, 44, 63, 69, 49, 86, 79, 37, 15, 82, 92, 23, 62]
# show_size(list_1)
#  *****
#  type = <class 'list'>, size = 264, object = [25, 23, 83, 13, 38, 60, 52, 44, 63, 69, 49, 86, 79, 37, 15, 82, 92, 23, 62]
# 	 type = <class 'int'>, size = 28, object = 25
# 	 type = <class 'int'>, size = 28, object = 23
# 	 type = <class 'int'>, size = 28, object = 83
# 	 type = <class 'int'>, size = 28, object = 13
# 	 type = <class 'int'>, size = 28, object = 38
# 	 type = <class 'int'>, size = 28, object = 60
# 	 type = <class 'int'>, size = 28, object = 52
# 	 type = <class 'int'>, size = 28, object = 44
# 	 type = <class 'int'>, size = 28, object = 63
# 	 type = <class 'int'>, size = 28, object = 69
# 	 type = <class 'int'>, size = 28, object = 49
# 	 type = <class 'int'>, size = 28, object = 86
# 	 type = <class 'int'>, size = 28, object = 79
# 	 type = <class 'int'>, size = 28, object = 37
# 	 type = <class 'int'>, size = 28, object = 15
# 	 type = <class 'int'>, size = 28, object = 82
# 	 type = <class 'int'>, size = 28, object = 92
# 	 type = <class 'int'>, size = 28, object = 23
# 	 type = <class 'int'>, size = 28, object = 62
# show_size(maximum)
#  *****
#  type = <class 'int'>, size = 28, object = 92
# show_size(minimum)
#  *****
#  type = <class 'int'>, size = 28, object = 13
# show_size(max_index)
#  *****
#  type = <class 'int'>, size = 28, object = 3
# show_size(min_index)
#  *****
#  type = <class 'int'>, size = 28, object = 16


##########################################################################
'''
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''


def sum_el(n, num=1):
    if n == 1:
        return num

    if n > 900:
        return 0.666666666666

    elif n > 1:
        return num + sum_el(n - 1, num / (-2))


lenth = int(input('Введите число элементов: '))

x = sum_el(lenth)           # добавил переменную для анализа

print(f'сумма = {sum_el(lenth)}')

print('show_size(lenth) \n *****')
show_size(lenth)
print('show_size(x) \n *****')
show_size(x)

##########################################################################
'''Результаты'''

# Введите число элементов: 18
# сумма = 0.6666641235351562
# show_size(lenth)
#  *****
#  type = <class 'int'>, size = 28, object = 18
# show_size(x)
#  *****
#  type = <class 'float'>, size = 24, object = 0.6666641235351562
#
# Process finished with exit code 0
