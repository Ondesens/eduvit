import math
#1.Сложение
def addition():
    try:
       summand = float(input('Введите первое слагаемое: '))
       summand_2 = float(input('Введите второе слагаемое: '))
    except Exception as e:
        print(e)
    else:
        return f'Сумма равна: {summand + summand_2}'
#2.Вычитание
def subtraction ():
    try:
        summand = float(input('Введите первое слагаемое: '))
        summand_2 = float(input('Введите второе слагаемое: '))
    except Exception as e:
        print(e)
    else:
        return f'Разность {summand} - {summand_2} = {summand+summand_2}'
#3.Умножение
def multiply ():
    try:
        multiplier = float(input('Введите первый множитель: '))
        multiplier_2 = float(input('Введите второй множитель: '))
    except Exception as e:
        print(e)
    else:
        return f' Произведение {multiplier} * {multiplier_2} = {multiplier*multiplier_2}'
#4.Деление
def division ():
    print('''Доступные операции
    1.Деление с остатком 
    2.Деление нацело c округление до ближайшего меньшего целого числа
    3.Деление нацело c округление до ближайшего большего целого числа''')
    try:
        operation = int(input('Введите номер желаемой операции: '))
        summand = float(input('Введите первое слагаемое: '))
        summand_2 = float(input('Введите второе слагаемое: '))
        if operation == 1:
            digits = int(input('Введите желаемое количество знаков после запятой: '))
            return f'Результат деления {summand} : {summand_2} = {round(summand/summand_2,digits)}'
        elif operation == 2:
            print()
            return f'Результат деления {summand} : {summand_2} = {math.floor(summand/summand_2)}'
        elif operation == 3:
            return f'Результат деления {summand} : {summand_2} = {math.ceil(summand/summand_2)}'
        else:
            return "Введено неверное число"
    except ZeroDivisionError as e:
        print(e)
#5. Возведение в степень
def exponentiation ():
    try:
        summand = float(input('число: '))
        exp = float(input('Введите степень: '))
    except Exception as e:
        print(e)
    else:
        return f' Число {summand} в степени {exp} = {summand**exp}'
#6.Факториал
def factorial():
    try:
        summand = int(input('Введите положительное целое число: '))
        fact=1
        for i in range(1,summand+1):
            fact*=i
        return f' Факториал числа {summand} равен {fact}'
    except Exception as e:
        print(e)
#7.Квадратный корень
def square():
    try:
        summand = float(input('Введите число: '))
        return f'Квадратный корень числа {summand} равен  {math.sqrt(summand)}'
    except Exception as e:
        print(e)
#8.Логарифм
def logarithmic():
    try:
        base = float(input('Введите основание логарифма: '))
        number = float(input('Введите логарифмируемое число: '))
        return f'Логарифм {number} по основанию {base} равен {math.log(number,base)}'
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

def switch_case(argument):
    if argument =='1':
        return addition()

    elif argument =='2':
        return subtraction()

    elif argument =='3':
        return multiply()

    elif argument =='4':
        return division()

    elif argument =='5':
        return exponentiation()

    elif argument =='6':
        return factorial()

    elif argument =='7':
         return square()

    elif argument =='8':
        return logarithmic()

    else:
        return '''Введено неверное значение
        Попробуйте снова)'''

while True:
    print('''Доступные операции:
    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление
    5. Возведение в степень
    6. Факториал
    7. Корень квадратный
    8. Логарифм
    -------------------------------''')
    arg= input("Введите номер желаемой операции или exit для завершения вычислений  : ")
    if arg == 'exit' or arg == "Exit":
        break
    print(switch_case(arg))
