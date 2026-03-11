#1
import math
gen = [i**2 for i in range(1, 11)]
#2
days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
week= {days[item]: item+1 for item in range(0,7)}
#3
teg =  ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
mn = set([i.lower() for i in teg])
#4
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
chet = [ num for num in numbers if num % 2 == 0]
#5
keys = [1,2,3,4,5]
fact = {keys[i]: math.factorial(keys[i]) for i in range(len(keys))}
print(f"1. {gen}\n"
      f"2. {week}\n"
      f"3. {mn}\n"
      f"4.  {chet}\n"
      f"5.  {fact}\n")
