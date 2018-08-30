__author__ = 'Мишин Егор Олегович'
'''
4. Определить, какое число в массиве встречается чаще всего
'''

from random import randint

list_1 = [randint(0, 9) for _ in range(1, 20)]


max_count = 1
max_cnum = 1
print(list_1)

for i in list_1:
    count = 0
    for k in list_1:
        if k == list_1[i]:
            count += 1
            num = k
    if count > max_count:
        max_count = count
        max_cnum = num
print(f'max_num = {max_cnum}, count = {max_count}')