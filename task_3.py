__author__ = 'Мишин Егор Олегович'
'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
    в одной находятся элементы, которые не меньше медианы, 
    в другой – не больше ее.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, 
то используйте метод сортировки, который не рассматривался на уроках.
'''

from random import randint


def median_find(array):
    if len(array) % 2 != 1:
        return print('Массив должен быть с нечетным числом элементов')

    for num1 in array:
        higher = []
        lower = []
        median = []
        for num2 in array:
            if num2 < num1:
                lower.append(num2)
            elif num2 > num1:
                higher.append(num2)
            else:
                median.append(num2)
        if abs(len(lower) - len(higher)) == len(median) - 1:
            return print(f'Медианой является число: {median[0]}\n'
                         f'{lower}{median}{higher}')


''' Генерируем рандомный список с неченым количеством элементов '''
my_list = [randint(-100, 99) / randint(1, 10) for i in range(2 * randint(1, 10) + 1)]
print(f' Исходный список: \n {my_list}')
median_find(my_list)

