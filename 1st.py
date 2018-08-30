__author__ = 'Мишин Егор Олегович'
'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9
'''

numbers = [_ for _ in range(2, 10)]
list_1 = [_ for _ in range(2, 100)]

for i in numbers:
    count = 0
    for k in list_1:
        if k % i == 0:
            count += 1
    print(f'В данном наборе {count} чисел кратно цифре {i}')
