__author__ = 'Мишин Егор Олегович'

'''
7. Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.
'''
n = int(input('Введите количество элементов n > 0: '))
k = 0
l = ''

for i in range(1, n+1):
    k += i
    l += f'{i} + '
    m = i*(i+1)/2

print(f'{l} = {i} * ({i} + 1) / 2')
print('\nПроверяем равеноство: ', k == m)
