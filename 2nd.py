__author__ = 'Мишин Егор Олегович'

'''
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
Объяснить полученный результат.
'''

print('\nИ с числами 5 и 6')
num1 = 5 and 6
print(f'num1 = {num1}')

print('\nИли с числами 5 и 6')
num2 = 5 or 6
print(f'num1 = {num2}')

print('\nПобитовый сдвиг 5 влево на 2')
num3 = 5 << 2
print(f'num1 = {num3}')

print('\nПобитовый сдвиг 5 вправо на 2')
num4 = 5 >> 2
print(f'num1 = {num4}')

print('\nПри сдвиге меняется двоичное представление числа. 5 в двоичном виде - 00000101, при сдвиге\n'
      'вправо происходит 00010100, что равняется 20, влево - 00000001, что равняется 1')