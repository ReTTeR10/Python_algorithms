__author__ = 'Мишин Егор Олегович'
'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
'''
import random


def sort_merge(array):
    if len(array) > 0:
        n = int(len(array) / 2)
        list_1 = array[:n]
        list_2 = array[n:]
        print(f'1й список {list_1}, 2ой список {list_2}')
    else:
        return print("Нечего сортировать")


# random.randint(0, 50)
my_list = [random.randint(0, 49) / random.randint(1, 10) for _ in range(1, 20)]  # создаем список вещественных чисел
print(my_list)

sort_merge(my_list)
