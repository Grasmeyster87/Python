my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk.copy())

new_disk = my_disk.copy()

new_disk['type'] = 'ssd'

print(my_disk)
print(new_disk)

print('id(my_disk): ', id(my_disk))
print('id(new_disk): ', id(new_disk))

print('len(my_disk): ', len(my_disk))
