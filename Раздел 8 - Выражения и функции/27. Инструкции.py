import datetime as DT


my_name = 'Vitaliy'  # Присвоение значения переменной

# Условная инструкция
if my_name:
    print(my_name)


def time_now():
    now = DT.datetime.now(DT.timezone.utc).astimezone()
    time_format = "%Y-%m-%d %H:%M:%S"
    print(f"{now:{time_format}}")

time_now()