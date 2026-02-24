list_1= list(input("Введите первый список: "))
list_2= list(input("Введите второй список: "))
for i in list_1:
    if i== " ":
        list_1.remove(i)
for i in list_2:
    if i== " ":
        list_2.remove(i)
print("Общие элементы: ", ' '.join(set(list_2) & (set(list_1))))
