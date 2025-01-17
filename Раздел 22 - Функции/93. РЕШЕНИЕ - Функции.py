def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


list1 = ['John', 'Frank', 'Tom']
list2 = [1, 2, 3]

res = merge_lists_to_dict(list1, list2)
print(res)

res_two = merge_lists_to_dict(['abc'], [{}, True, 100])
# res_two = merge_lists_to_dict(['abc'], [{}])
print(res_two)

res_three = merge_lists_to_dict(['a', True, 100], ['abc'])
# res_three = merge_lists_to_dict(['a'], ['111'])
print(res_three)
