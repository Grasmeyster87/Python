my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2, 
}

other_motorbike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati',
}

print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))