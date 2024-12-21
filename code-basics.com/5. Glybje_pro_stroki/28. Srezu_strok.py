value = '12-08-2034'

print(value[6])
print(value[9])

year = value[6:10]
print(year)

value1 = 'Hexlet'

value1[3:]  # 'let'
value1[:3]  # 'Hex'

value = 'Hexlet'
value[1:5:2]  # el
# 1:5 это 'exle'
# шаг 2 это каждый второй, то есть 'e' и 'l'

value = 'Hexlet'
value[:5:2]  # 'Hxe'
value[1::2]  # 'elt'
"""
Шаг может быть отрицательным, в таком случае он берется с конца.
Из этого вытекает самый популярный способ использования шага переворот строки:
"""
value = 'Hexlet'
# Пропускаем обе границы
print('\n', value[::-1])  # 'telxeH'

value = 'Hexlet'
# Символ с индексом 1 не будет включен в подстроку
value[4:1:-1]  # 'elx'


value = 'Hexlet'
start = 1
end = 5
value[start:end]  # 'exle'

value = 'Hexlet'
# value[::] = 'Hexlet'  # Вся строка
# value[:] = 'Hexlet'  # Вся строка
# value[::2] = 'Hxe'  # Четные по порядку символы
# value[1::2] = 'elt'  # Нечетные по порядку символы
# value[::-1] = 'telxeH'  # Вся строка в обратном порядке
# value[5:] = 't'  # Строка, начиная с шестого символа
# value[:5] = 'Hexle'  # Строка до шестого символа
# value[-2:1:-1] = 'elx'  # Все символы с предпоследнего до третьего
# включительно, в обратном порядке

# Во всех случаях выборки от большего индекса к меньшему нужно указывать шаг

value = 'Hexlet'

# BEGIN (write your solution here)
print(value[2:5])
# END
