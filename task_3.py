def record_str(text,filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i,line in enumerate(lines,1):
        if i % 2 == 0:
            print(f'Строка {i}: {line} ')
    if len(lines) < 2:
        print("В файле недостаточно строк для вывода четных строк")

record_str("Четвёртая строка", "test.txt")
