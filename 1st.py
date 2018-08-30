__author__ = 'Мишин Егор Олегович'

'''
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, 
а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' 
в качестве знака операции. 
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
и снова запрашивать знак операции. 
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''

print('\n----Добро пожаловать в КАЛЬКУЛЯТОР3000!----')


def user_input():

    return input('\nЖелаемое действие? (+,-,*,/, 0 - выход) ')


def check_input(ans):
    if ans != '+' and ans != '-' and ans != '*' and ans != '/' and ans != '0':
        print('Неверное действие')
        return False
    else:
        pass


ans = user_input()
if ans != '+' and ans != '-' and ans != '*' and ans != '/' and ans != '0':
    print('Неверное действие')
    ans = user_input()
while check_input(ans) is False:
    ans = user_input()
while ans != '0':
    while check_input(ans) is False:
        ans = user_input()
    num1 = float(input('\nВведите первое число'))
    num2 = float(input('\nВведите второе число'))
    if ans == '+':
        print(f'Результат {num1} {ans} {num2} = {num1 + num2}')
        ans = user_input()
    elif ans == '-':
        print(f'Результат {num1} {ans} {num2} = {num1 - num2}')
        ans = user_input()
    elif ans == '*':
        print(f'Результат {num1} {ans} {num2} = {num1 * num2}')
        ans = user_input()
    elif ans == '/':
        if num2 == 0:
            print('Деление на 0. Попался!)')
            ans = user_input()
        else:
            print(f'Результат {num1} {ans} {num2} = {num1 / num2}')
            ans = user_input()
    else:
        print('Неверное действие')
        ans = user_input()
print('До свидания!')
