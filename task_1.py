list_1= list(input ("Введите числа через пробел: "))
exp = int(input("ведите степень: "))
s=''
ls=[]
ls_2=[]
for i in list_1 :
    if i !=' ' and i!='' :
        s+=i
    if (i == " " or i== list_1[len(list_1)-1]) and s!='':
        ls.append(s)
        s =""
for i in ls:
    if i.lstrip('-').isdigit() == True:
        ls_2.append(int(i)**exp)
    else:
        for j in range(exp-1):
            i+=i
        ls_2.append(i)
print(ls_2)
