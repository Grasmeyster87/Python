my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2, 
}
key_name = 'brand'

my_motorbike[key_name] = 'BMW'

print(my_motorbike)

my_motorbike1 = {
    'brand': 'Ducati',
    'engine_vol': 1.2, 
    'price_info': {
        'price': 25000,
        'is_available': True,
    }
}

print(my_motorbike1['price_info']['price'])

print(my_motorbike1['price_info']['is_available'])

# -------------- Переменные для создания словарей -------------

brand1 = 'Honda'
bike_price1 = 20_000
engine_volume = 1.2

my_motorbike_Honda = {
    'brand1': brand1,
    'price': bike_price1,
    'engine_vol': engine_volume,
}

print(my_motorbike_Honda)