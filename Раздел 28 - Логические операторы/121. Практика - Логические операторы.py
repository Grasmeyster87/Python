my_list = [1, 2]
other_list = ['a', 'b']

print(not my_list)
print(not not my_list) 

print(my_list or other_list)
print(len(my_list) > 0 or other_list)
print(len(my_list) < 0 or other_list)

my_dict = {}
print(my_list and my_dict)
print(bool(my_list and my_dict))

# Если оператор не пустой
my_list and print("List is not empty") # and  операток короткого замыканий

# Задание
dict1 = {'1': '1', '2': '2'}
dict2 = {'2': '2', '1': '1'}

print(dict1 == dict2 and "Dictionaries are equal")