# str станет int
number = int('345')
print(number)  # => 345


value = '0'
# Внутри скобок можно указывать переменную
converted_value = int(value)
print(converted_value)  # => 0

# Или конкретное значение
converted_value2 = int('10')
print(converted_value2)  # => 10

converted_value3 = int(False)
print(converted_value3)  # => 0

converted_value4 = int(True)
print(converted_value4)  # => 1

# Если преобразуется число с плавающей точкой
# то отбрасывается вся дробная часть
converted_value5 = int(3.5)
print(converted_value5)  # => 3

value = str(10)
print(value)  # '10'

value2 = str(True)
print(value2)  # 'True'

value3 = float(5)
print(value3)  # 5.0

# Неявно выполняется код float(3) + 1.2
value = 3 + 1.2
print(value)  # => 4.2

value = 2.9

# BEGIN (write your solution here)
print(str(int(value)) + ' times')

# END