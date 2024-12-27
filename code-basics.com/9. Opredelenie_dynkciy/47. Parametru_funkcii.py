def get_last_char(text):
    return text[-1]


# Передача параметров напрямую без переменных
get_last_char("Hexlet")  # t
# Передача параметров через переменные
name1 = 'Hexlet'
get_last_char(name1)  # t
name2 = 'Goo'
get_last_char(name2)  # o


def get_last_char(string):
    return string[-1]

# Внутри функции string будет равна 'hexlet'


get_last_char('hexlet')  # t

# Внутри функции string будет равна 'code'
get_last_char('code')  # e

# Внутри функции string будет равна 'Winter is coming'
# Имя переменной снаружи не связанно с именем переменной в определении функции
text = 'Winter is coming'
get_last_char(text)  # g

round(10.23456, 3)  # 10.235

# Первый параметр — что ищем
# Второй параметр — на что меняем
'google'.replace('go', 'mo')  # moogle


def truncate(text, length):
    return f'{text[:length]}...'


print(truncate('hexlet', 2))
