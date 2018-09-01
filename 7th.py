__author__ = 'Мишин Егор Олегович'
"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint


def minimum(my_list):
    min_el = my_list[0]
    min_in = 0
    for i, item in enumerate(my_list):
        if item < min_el:
            min_el = item
            min_in = i
    return min_el, min_in


list_1 = [randint(-9, 9) for _ in range(1, 20)]

print(f'Наш массив: {list_1}')
print(f'Самое маленькое число в массиве: {minimum(list_1)[0]}')    # все же классная вещь f-строки)

list_1.pop(minimum(list_1)[1])

print(f'Второе по малости число или равное: {minimum(list_1)[0]}')
