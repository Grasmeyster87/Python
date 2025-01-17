my_list = [1, 2, 3]
print(id(my_list))

other_list = [1, 2, 3]
other_list.append(4)

print(id(other_list))

print(id([1, 2, 3]))

info = {
    'name': 'Bogdan',
    'is_instructor': True,
}
info_copy = info
info['reviews_qty'] = 100

print(info['reviews_qty'])
print(info_copy['reviews_qty'])

other_info = {
    'name': 'Bogdan',
    'is_instructor': True,
}
