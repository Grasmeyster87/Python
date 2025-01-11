my_nums = [10, 50, 0, 5, 5, 25, 100]
# print(dir(my_nums))

res_5 = my_nums.count(5)
res_25 = my_nums.count(25)
res_insert = my_nums.insert(2, -5)
# my_nums.clear()
my_nums.extend('abc')

print('my_nums.count(5): ', res_5)
print('my_nums.count(25): ', res_25)
print('my_nums.insert(-5): ', my_nums)
print('my_nums.clear()', my_nums)


# other_nums = my_nums  #  Создание второй ссылки на объект
other_nums = my_nums.copy()  # копирование объекта
# other_nums = my_nums.[:]  # копирование объекта
# other_nums = list(my_nums)  # копирование объекта

print('id(my_nums) - ', id(my_nums))
print('id(other_nums) - ', id(other_nums))

my_nums.append(3)
other_nums.clear()
print(my_nums, "\n", other_nums)
