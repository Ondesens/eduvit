dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
mn=set(dct.keys())
s=[]
for i in mn:
    s.append(dct.get(i))
print(f'Множество ключей: {set(mn)}')
print(f'Множество значений: {set(s)}')
for i in range(len(mn)):
    mn.add(s[i])
print(f'Объединение множеств: {mn}')
