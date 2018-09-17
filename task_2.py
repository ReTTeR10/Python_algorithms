__author__ = 'Мишин Егор Олегович'
'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
'''
import random


def sort_merge(array):
    if len(array) > 1:
        mid = len(array) // 2  # делим пополам
        left = array[:mid]     # левая половина
        right = array[mid:]    # правая половина

        sort_merge(left)       # разбиваем половины еще на половины
        sort_merge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif len(array) < 1:
        return print("Число элементов массива должно быть больше 1 элемента")
    return array


my_list = [random.randint(0, 49) / random.randint(1, 10) for _ in range(1, 20)]  # создаем список вещественных чисел
# my_list = []
print(f'Исходный массив: \n {my_list}')
print(f'Отсортированный массив: \n {sort_merge(my_list)}')
