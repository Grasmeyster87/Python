
my_dict = {
    '1': 1,
    '2': 2,
    'a': 'first commit',
    'b': 'second commit',
    'c': 'third commit',
    'my_list': [1, 2, 3]
}


def dict_to_list(dict1):
    res_list = []
    for k, v in dict1.items():
        if type(v) == int:
            v *= 2
        res_list.append((k, v))
    return res_list


print(dict_to_list(my_dict))


def filter_list(list1, type1):
    list1_new = []
    for el in list1:
        if type(el) == type1:
            list1_new.append(el)
    return list1_new


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
