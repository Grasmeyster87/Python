my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2, 
}
# print(my_motorbike['model'])
print(my_motorbike.get('model'))  #  возврат None
print(my_motorbike.get('qty', 0)) # замена None на 0

print('\n\n')
print(my_motorbike.get('brand')) 
print(my_motorbike.get('price')) 
print(my_motorbike.get('qty', 0)) 
