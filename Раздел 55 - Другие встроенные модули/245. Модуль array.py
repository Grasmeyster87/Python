from array import array

my_int_array = array('i', [4, 5, 5, 10, 5, 7])

# print('my_int_array - ', my_int_array)  # my_int_array -  array('i', [4, 5, 5, 10, 5, 7])
# print('type(my_int_array) - ', type(my_int_array))  # type(my_int_array) -  <class 'array.array'>

# my_int_array.append(15)  # type(my_int_array) -  <class 'array.array'>

# print(my_int_array)  # array('i', [4, 5, 5, 10, 5, 7, 15])
# print('Включений числа 5 - ', my_int_array.count(5))  # Включений числа 5 -  3

# my_int_array.pop()  # Включений числа 5 -  3

# print(my_int_array)   # array('i', [4, 5, 5, 10, 5, 7])s

# print('len(my_int_array) - ', len(my_int_array))  # len(my_int_array) -  6

# for elem in my_int_array:
#     print(elem)

# print('my_int_array[1] - ', my_int_array[1])  # my_int_array[1] -  5

with open('./Раздел 55 - Другие встроенные модули/files/my_array.bin', 'wb') as my_file:  # wb режим бинарной записи
    my_int_array.tofile(my_file)


imported_array = array('i')

with open('./Раздел 55 - Другие встроенные модули/files/my_array.bin', 'rb') as my_file:  # wb режим бинарной записи
    imported_array.fromfile(my_file, 3)
    print(imported_array)

imported_array.reverse()
print(imported_array)