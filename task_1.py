__author__ = 'Мишин Егор Олегович'
'''
1. Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()
'''

from random import choice
from string import ascii_lowercase


my_string = ''   # формируем рандомную строку
num = int(input('Введите длину строки: '))
my_string += ''.join(choice(ascii_lowercase) for i in range(num))
print(f'Ваша строка: \n {my_string}')

our_hash = []

for i in range(len(my_string) + 1):
    for j in range(i + 1, len(my_string) + 1):
        if (not hash(my_string[i:j]) in our_hash) and (not my_string[i:j] == my_string):
            our_hash.append(hash(my_string[i:j]))

print(f'{len(our_hash)} подстрок(а) в исходной строке: \n {my_string}')

'''
Был такой пример при num = 232
'''
#
# Ваша строка:
#  hfbsxyuhlkgeodaqlwvregzousuufgwjzwtglngjrqqdjxxzzgbhnakwatnstwgblhsawzcqumobnchggkxesuqjlepsdlxapkcxbqiztfcntanhrqwrgoolnjfgkqdetkcrowrefvefrsvpqkvcbaufydbzayhuttgjxmigvlwxzaemlmdaiwibsvieczkiawiwresoomlfjpucvwcnopvfouqlchfqectljooq
#
# 26783 подстрок в исходной строке:
#  hfbsxyuhlkgeodaqlwvregzousuufgwjzwtglngjrqqdjxxzzgbhnakwatnstwgblhsawzcqumobnchggkxesuqjlepsdlxapkcxbqiztfcntanhrqwrgoolnjfgkqdetkcrowrefvefrsvpqkvcbaufydbzayhuttgjxmigvlwxzaemlmdaiwibsvieczkiawiwresoomlfjpucvwcnopvfouqlchfqectljooq |

