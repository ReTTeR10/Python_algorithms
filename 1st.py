__author__ = 'Мишин Егор Олегович'
'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
Примечание: 4 квартала - это 4 разных прибыли ;-)
'''
from collections import namedtuple

Company = namedtuple('Сompany', 'name quarter1 quarter2 quarter3 quarter4 average')  # создаем namedtuple
n = int(input('Сколько компаний для анализа? '))

all_company = []
lower = []
higher = []

for i in range(n):                      # заполняем
    name = input('Введите название фирмы: ')
    quarter1 = int(input('Прибыль за 1ый квартал: '))
    quarter2 = int(input('Прибыль за 2ый квартал: '))
    quarter3 = int(input('Прибыль за 3ий квартал: '))
    quarter4 = int(input('Прибыль за 4ый квартал: '))
    average = (quarter1 + quarter2 + quarter3 + quarter4) / 4
    our_company = Company(name, quarter1, quarter2, quarter3, quarter4, average)  # передаем введеные значения в перемен
    all_company.append(our_company)         # добавляем в список

summ_profit = 0

for line in all_company:
    summ_profit += (line.quarter1 + line.quarter2 +
                    line.quarter3 + line.quarter4)

total_average = summ_profit / (4 * n)
print(f'Общее средняя выручка: {total_average}')

for line in all_company:
    if line.average < total_average:    # определяем какие компании меньше заработали, а какие больше
        lower.append(line.name)
    else:
        higher.append(line.name)

print(f'Кто меньше - {lower}, больше - {higher}')


''' Тут первый вариант решения, но я так и не понял как на лету передавать в этот namedtuple значения'''

'''
n = int(input('Сколько компаний для анализа? '))
i = 0
company = []
profit = {}
average = []
while i != n:
    quartal = ['name', 'first', 'second', 'third', 'fourth', 'profit']
    profit = 0
    Company_name = namedtuple('Company_name', quartal)
    company.append(Company_name(input('name'), input('first'), input('second'), input('third'), input('fourth'), 0))

    company[i]._asdict()
    company[i]._replace(profit=company[i].first + company[i].second + company[i].third + company[i].fourth)
    i += 1
    average = 0
for line in company:
    print(line)
'''