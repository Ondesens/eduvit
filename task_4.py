str = input("Введите строку: ").lower()
str = str + " "
s = ""
ls = []
mn = set()

for i in range(len(str)):
    simvol = str[i]
    if simvol != " ":
        s = s + simvol
    else:
        if s != "":
            ls.append(s)
            mn.add(s)
            s = ""
print(ls)
for j in mn:
    print(f"{j} : {ls.count(j)}")
