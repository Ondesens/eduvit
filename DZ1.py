#1. Форматирование строк

name=input("Ваше имя: ")
surname =input("Фамилия: ")
age =input("возраст: ")
print(f'Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет')
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name,surname,age))

#2. Четность числа

number=input("Введите число: ")
if number.isdigit()==False:
    print("Ошибка: введено не число")
elif int(number)%2==0 :
    print(f'Число {number} является чётным')
else:
    print(f'Число {number} не является чётным')

#3. Проверка возраста

age=input("Введите ваш возраст: ")
if age.lstrip('-').isdigit()==False:
    print("Ошибка: введено не число!")
elif int(age)<0:
    print("Ошибка: возраст не может быть отрицательным!")
elif int(age)>=18:
    print("Вы совершеннолетний.")
else:
    print("Вы несовершеннолетний.")

#4. Длина числа

while True:
    number = input("Введите число: ")
    if number=="exit":
        print("Выход из программы...")
        break
    if number.lstrip('-').isdigit()==False:
        print("Ошибка: данные не являются числом.")
        continue
    if "-" in number:
        print(f'В этом числе {len(number)-1} цифры')
    else:
        print(f'В этом числе {len(number)} цифры')
    continue




