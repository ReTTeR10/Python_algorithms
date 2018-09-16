__author__ = 'Мишин Егор Олегович'
'''
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). 
Вывести на экран исходный и отсортированный массивы.
'''
from random import randint


def bubble_sort(a):
    n = len(a)
    for j in range(n-1):
        for i in range(n-j-1):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a


my_list = [randint(-100, 99) for _ in range(1, 20)]
print(f'Начальный список: \n {my_list}')
print(f'Отсортированный списое: \n {bubble_sort(my_list)}')
