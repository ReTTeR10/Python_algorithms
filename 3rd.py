__author__ = 'Мишин Егор Олегович'

'''
По введенным пользователем координатам двух точек вывести уравнение прямой, 
проходящей через эти точки.
'''

points = input('Введите через пробел x1, y1, x2, y2: ').split(' ')
x1, y1, x2, y2 = int(points[0]), int(points[1]), int(points[2]), int(points[3])
print(x1, y1, x2, y2)
if x1 == x2:
    print(f'x = {x1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1
    print(f'y = {k}x + {b}')

