my_nums = (10, 5, 100, 0, 5, 5)

print(type(my_nums))
#  del my_nums68[1]

# print('\nmy_nums.count(5): ', my_nums.count(5))
# print('\nmy_nums.index(5): ', my_nums.index(5))

# index_one = my_nums.index(5)
# поиск с индекса index_one включительно
# index_two = my_nums.index(5, index_one + 1)
# index_three = my_nums.index(5, index_two)

# print('index_two: ', index_two)
# print('index_three: ', index_three)

my_list = list(my_nums)
my_list.append(7)

print(my_list)
print(my_nums)

my_nums = tuple(my_list)
print(my_nums)

my_touple = tuple('abcd')
my_touple1 = tuple({'first': 1, 'second': True})
print(my_touple)
print(my_touple1)