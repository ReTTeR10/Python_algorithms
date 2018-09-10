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

'''
Не успел решить задачу правильно(в столбик), но алгоритм понятен. Если успею доделать то обязательно приложу его в гит
отдельным файлом.
'''


sixteen = {str(a): a for a in range(16)}    # словарь для перевода в 10ую систему
sixteen2 = {a: str(a) for a in range(16)}   # для обратного перевода


for x in range(10, 16):               # меняем цифры на буквы
    sixteen[chr(x+87)] = sixteen.pop(str(x))
    sixteen2[x] = chr(x + 87)


def sixteen_ten(num16):               # функция перевода в 10ую систему
    length = len(num16) - 1           # так как переводим из 16-ой то и умножаем на 16**
    num10 = 0
    for i in num16:
        for key, value in sixteen.items():
            if i == key:
                num10 += value * (16 ** length)
                length -= 1
    return num10


def ten_sixteen(num10):                # для обраного перевода
    length = len(str(num10)) - 1
    num16 = deque()
    while length != 0:
        num16.appendleft(num10 % 16)    # так как 16-ая система, то и делим на 16.
        num10 = num10 // 16
        length -= 1
    for i, item in enumerate(num16):
        for key, value in sixteen2.items():
            if item == key:
                num16[i] = value
    return num16


num16_1 = [_ for _ in input('Введите первое число(пример a2): ')]
num16_2 = [_ for _ in input('Введите второе число(пример с4f): ')]

print('*' * 20, '=D','cheatcode activated', '=D', '*' * 20)

summa = ten_sixteen(sixteen_ten(num16_1) + sixteen_ten(num16_2))           # IDDQD
mult = ten_sixteen(sixteen_ten(num16_1) * sixteen_ten(num16_2))             # IDKFA


print(f'{num16_1} + {num16_2} = {summa}\n {num16_1} * {num16_2} = {mult}')



