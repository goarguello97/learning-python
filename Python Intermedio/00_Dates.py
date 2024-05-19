### Dates ###

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

timestamp = now.timestamp()

print(timestamp)

year_2024 = datetime(2024, 5, 18)

print_date(year_2024)


current_time = time(20, 4, 30)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 1, 8)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)


init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)
