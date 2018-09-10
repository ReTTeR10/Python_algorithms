__author__ = 'Мишин Егор Олегович'
'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. 
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque


sixteen = {str(a): a for a in range(16)}
sixteen2 = {a: str(a) for a in range(16)}


for x in range(10, 16):
    sixteen[chr(x+87)] = sixteen.pop(str(x))
    sixteen2[x] = chr(x + 87)


def sixteen_ten(num16):
    length = len(num16) - 1
    num10 = 0
    for i in num16:
        for key, value in sixteen.items():
            if i == key:
                num10 += value * (16 ** length)
                length -= 1
    return num10


def ten_sixteen(num10):
    length = len(str(num10)) - 1
    num16 = deque()
    while length != 0:
        num16.appendleft(num10 % 16)
        num10 = num10 // 16
        length -= 1
    for i, item in enumerate(num16):
        for key, value in sixteen2.items():
            if item == key:
                num16[i] = value
   # num16.reverse()
    return num16


# def summa(num1, num2):
#     num1 = sixteen_ten(num1)
#     num2 = sixteen_ten(num2)



num16_1 = [_ for _ in input('Введите число:')]
num16_2 = [_ for _ in input('Введите число:')]

summa1 = ten_sixteen(sixteen_ten(num16_1) + sixteen_ten(num16_2))
mult = ten_sixteen(sixteen_ten(num16_1) * sixteen_ten(num16_2))


print(f'sum = {summa1}, mult = {mult}')


