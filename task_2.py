import math
def simple_number():
    begin_num=2
    while True:
        flag = True
        for j in range(2 , math.floor((begin_num**0.5))+1):
            if begin_num % j == 0 :
                flag = False
        if flag :
            yield begin_num

        begin_num+=1

sml_number=simple_number()
count= int(input("Введите желаемое количество простых чисел : "))
for _ in range(count):
    print(next(sml_number))





