my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2, 
}

print(my_motorbike['brand'])

print(my_motorbike['price'])

# -------------- Изменение значений ------------------------

my_motorbike['price'] = 2000

print(my_motorbike['price'])
print('\ndir(my_motorbike):', dir(my_motorbike))
my_motorbike['price'] = 7000

my_motorbike['is_new'] = True

print(my_motorbike)

# ------------ Удаление элементов ---------------------------

del my_motorbike['engine_vol']

print(my_motorbike)
