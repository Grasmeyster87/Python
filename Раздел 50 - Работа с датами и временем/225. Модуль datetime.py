from datetime import date
from datetime import time
from datetime import datetime

# ---------------- date----------------
# print(type(date))  # <class 'type'>

# my_date = date(2100, 4, 5)
# print(my_date)

# print(my_date.day)
# print(my_date.month)
# print(my_date.year)

# print(my_date.isocalendar())
# ---------------- time ----------------
# my_time = time(18, 10, 45)

# print(my_time)
# print(my_time.hour)
# print(my_time.minute)
# print(my_time.second)

# ---------------- datetime-------------
my_datetime = datetime(2025, 2, 4, 12, 50, 45)
print(my_datetime)

date_now = (my_datetime.year, my_datetime.month, my_datetime.day,
            my_datetime.hour, my_datetime.minute, my_datetime.second,
            my_datetime.microsecond)
print('date_now: ', date_now)

print(my_datetime.isoformat())
print(my_datetime.now().isoformat())
print(my_datetime.now().microsecond)
