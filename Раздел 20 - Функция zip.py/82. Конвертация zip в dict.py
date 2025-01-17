fruits = ['apple', 'banan', 'lime', 'orange']

# quantities = [100, 70, 50]
# quantities = '1573'


availability = [True, False, False, True]

# fruit_qtys_zip = zip(fruits, quantities, availability)
fruit_qtys_zip = zip(fruits, availability)

print(fruit_qtys_zip)

fruit_qtys_list = list(fruit_qtys_zip)
fruit_qtys_dict = dict(fruit_qtys_zip)

# {'apple': True, 'banan': False, 'lime': False, 'orange': True}
print(fruit_qtys_list)
print(fruit_qtys_dict)

# --------------------- Задание -----------------------

shop_price = ['12', '20', '24']
shop_supplies = ['apple', 'pear', 'cherries']

res_zip = zip(shop_supplies, shop_price)
res_list = list(res_zip)
res_dict = dict(zip(shop_supplies, shop_price))  # не подставляется переменная

print('\n', res_list)
print('\n', res_dict)
