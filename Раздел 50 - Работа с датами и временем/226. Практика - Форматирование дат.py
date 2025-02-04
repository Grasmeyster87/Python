
from datetime import datetime

# ---------------- datetime-------------
my_datetime = datetime(2025, 2, 4, 12, 50, 45)

print('my_datetime.now() ', my_datetime.now())
print('my_datetime.strftime(\'%d-%b-%Y\')', my_datetime.strftime('%d-%b-%Y'))
print('my_datetime.strftime(\'%d-%m-%Y\')', my_datetime.strftime('%d-%m-%Y'))
print('my_datetime.strftime(\'%d/%m/%Y\')', my_datetime.strftime('%d/%m/%Y'))
print('my_datetime.strftime(\'%d-%m-%Y %H:%M:%S\')',
      my_datetime.strftime('%d-%m-%Y %H:%M:%S'))

date_str = '04/02/2025'

converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print('converted_date ', converted_date)
