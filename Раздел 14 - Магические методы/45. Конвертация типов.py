"""
Функции для конвертации типов
str()
float()
tuple()
int()
list()
set()

"""
# print('10' + 5)  # TypeError: can only concatenate str (not "int") to str
# print(5 + '10')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ------ Пример №1 ------
int_num = 5
float_num = 4.5

print('int_num + float_num: ', int_num + float_num)
print('float_num + int_num: ', float_num + int_num)

print('int_num.__add__(float_num): ', int_num.__add__(float_num))
print('float_num.__radd__(int_num): ', float_num.__radd__(int_num))

# ------ Пример № 2 ------
bool_val = True
int_val = 7

print('bool_val + int_val: ', bool_val + int_val)
print('int_val + bool_val: ', int_val + bool_val)
