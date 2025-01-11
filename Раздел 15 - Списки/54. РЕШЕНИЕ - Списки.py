arr_1 = [12, 'a', 14.14, True, [1]]

print(arr_1)

res_pop = arr_1.pop(2)

print('\nlen(arr_1): ', len(arr_1))

arr_1.reverse()

arr_2 = [1, 'a']

arr_1.extend(arr_2)
print(arr_1)

first_list = [1, 'a']
second_list = [2, 'b']
# third_list = first_list + second_list
# print(dir(first_list + second_list))

third_list = first_list.__add__(second_list)
print(third_list)

print('\nfirst_list: ', first_list)
print('\nsecond_list: ', second_list)
print('\nthird_list: ', third_list)
