fruits = ['apple', 'banan', 'lime', 'orange']

# quantities = [100, 70, 50]
quantities = '1573'


availability = [True, False, False, True]

fruit_qtys_zip = zip(fruits, quantities, availability)

print(fruit_qtys_zip)

fruit_qtys_list = list(fruit_qtys_zip)
print(fruit_qtys_list)