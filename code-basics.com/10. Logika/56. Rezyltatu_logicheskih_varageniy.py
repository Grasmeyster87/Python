print(0 or 1)  # 1

print(0 or False or '' or [] or 42 or "Hello")  # 42


print(42 and "Hello" and [] and 0)  # []

value = 1 or ''  # Примеры
234 or ''  # 234
'hexlet' or ''  # 'hexlet'
None or ''  # ''

# Это можно сделать, если использовать знания, полученные выше:

# число четное
result = 10 % 2 == 0 and 'yes' or 'no'  # 'yes'
# или сразу печатаем на экран
print(10 % 2 == 0 and 'yes' or 'no')  # => 'yes'
# число нечетное
print(11 % 2 == 0 and 'yes' or 'no')  # => 'no'


# Для четного
# 1 шаг
10 % 2 == 0  # True
# 2 шаг
True and 'yes'  # Результат — 'yes'
# Проверка на or выполняется, но правая часть не исполняется, так как сразу возвращается 'yes'

# Для нечетного
# 1 шаг
11 % 2 == 0  # False
# 2 шаг
False and 'yes'  # Результат — ложь, проверяем дальше
# 3 шаг
False or 'no'  # Выбирается и возвращается 'no'


# При двойном отрицании итоговое значение равно начальному:

answer = True
print(not not answer)  # => True

answer = 'python'
print(not answer)  # => False
print(not not answer)  # => True


def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'
