int_num = 50
float_num = 50.5
str_val = 'abc'

# print('int_num + float_num: ', int_num + float_num)
print(int_num.__mul__(float_num))
print(int_num.__mul__('abc'))  # Notimplemented

print(float_num.__rmul__(int_num))
# не реализован метод умножения строки на нецелое число
print(int_num * str_val)
