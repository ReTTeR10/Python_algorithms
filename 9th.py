__author__ = 'Мишин Егор Олегович'

'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
'''


count = int(input('\nСколько чисел будем вводить? '))
maximum = 0
max_num = 0
while count != 0:
    num = input('\nВведите число: ')
    summa = 0
    for i in num:
        summa += int(i)
    if summa > maximum:
        maximum = summa
        count -= 1
        max_num = num
    else:
        count -= 1
print(f'максимальное число по сумме: {max_num}, а сумма = {maximum} ')