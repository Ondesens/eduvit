str = input("Введите строку: ")
s=""
ls=[]
mn=set()
k=1
for i in str :
    if i !=' ' and i!='' :
        s+=i
    if (i == " " or i== str[len(str)-1]) and s!='':
        mn.add(s)
        ls.append(s)
        s =""
        k+=1
print(ls)
for  i in mn:
    print(f'{i} : {ls.count(i)}')



