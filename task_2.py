import random
import statistics
import math
list_1 = []
for i in range(100):
    list_1.append(random.randint(1,100))
# Среднее
mean = statistics.mean(list_1)
# Медиана
median = statistics.median(list_1)
#list[int]
square_sum = round(math.sqrt(sum(list_1)),2)
#Округленное значение квадратного корня из суммы всех чисел
st_dev = round(statistics.stdev(list_1),2)
# Вывод
print(f'Среднее: {mean}, Медиана: {median}, Стандартное отклонение: {st_dev}, Корень из суммы: {square_sum}')
