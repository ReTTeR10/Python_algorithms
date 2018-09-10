__author__ = 'Мишин Егор Олегович'
'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
Примечание: 4 квартала - это 4 разных прибыли ;-)
'''
from collections import namedtuple

Company = namedtuple('Сompany', 'name quarter1 quarter2 quarter3 quarter4 average')
n = int(input('Сколько компаний для анализа? '))

all_company = []
lower = []
higher = []

for i in range(n):
    name = input('Введите название фирмы: ')
    quarter1 = int(input('Прибыль за 1ый квартал: '))
    quarter2 = int(input('Прибыль за 2ый квартал: '))
    quarter3 = int(input('Прибыль за 3ий квартал: '))
    quarter4 = int(input('Прибыль за 4ый квартал: '))
    average = (quarter1 + quarter2 + quarter3 + quarter4) / 4
    our_company = Company(name, quarter1, quarter2, quarter3, quarter4, average)
    all_company.append(our_company)

summ_profit = 0

for line in all_company:
    summ_profit += (line.quarter1 + line.quarter2 +
                    line.quarter3 + line.quarter4)

total_average = summ_profit / (4 * n)
print(f'Общее средняя выручка: {total_average}')

for line in all_company:
    if line.average < total_average:
        lower.append(line.name)
    else:
        higher.append(line.name)

print(f'Кто меньше - {lower}, больше - {higher}')
