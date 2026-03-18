import random
import string
import os

def name_file():
    s=string.ascii_letters + string.digits
    files_names =[]
    for i in range(10):
        nme_file = ''
        for _ in range(8):
            nme_file += random.choice(s)
        with open(f'D:\\Курс 2\\Семестр 2\\Курс eduvit\\DZ_5\\Файлы\\{nme_file + ".txt"}', 'w') as file:
            files_names.append(nme_file+ ".txt")
    return files_names
for i in name_file():
    print(os.path.abspath(i))







