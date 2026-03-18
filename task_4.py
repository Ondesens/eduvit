from datetime import datetime,timedelta
import random
start_date = datetime(2021,3,13)
start_date= datetime.date(start_date)
end_date = datetime(2026,3,13)
end_date= datetime.date(end_date)
days = (end_date - start_date).days
random_dates = []
for  i in range(10):
    random_date = random.randint(0, days)
    random_dates.append(random_date)
random_dates = sorted(random_dates)

for  i in range(1,len(random_dates)):
    days = timedelta(random_dates[i] - random_dates[i-1])
    print(f'Разница между {start_date + timedelta( days = random_dates[i - 1])} и {start_date + timedelta( days = random_dates[i])}: {days.days} дней')

