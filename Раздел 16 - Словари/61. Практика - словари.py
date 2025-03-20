my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk)
print(id(my_disk), '\n')

print('\n\n', my_disk.__doc__)
print('\n\n', my_disk.items())
print(type(my_disk.items()), '\n')

print('\n\n', my_disk.keys())
print(list(my_disk.keys()))
print(my_disk.popitem())
# hdd значение по умолчанию если такого ключа нет
print(my_disk.get('type', 'hdd'))

print(my_disk)