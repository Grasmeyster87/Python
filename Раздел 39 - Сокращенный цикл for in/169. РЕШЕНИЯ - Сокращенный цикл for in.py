
# my_dict1 = {
#     'treck_№1':'Anastimoza Hruzantemu STALKER 2 Radio2k ',
#     'treck_№2': 'Lyapis Trubetskoy - Ау',
# }

# my_dict2 = {k: v.upper() for k, v in my_dict1.items() }

# print(my_dict2)

my_list1 = ['abc', 'Anastimoza Hruzantemu STALKER 2 Radio2k ',
            'Lyapis Trubetskoy - Ау']

my_list2 = [el for el in my_list1 if len(el) > 3]

print(my_list2)
