
fruits = {'apple', 'cherry', 'rasbery'}
other_fruits = {'apple', 'cherry', 'rasbery'}

print('fruits == other_fruits: ', fruits == other_fruits)  # True

print('fruits.__eq__(other_fruits): ', fruits.__eq__(other_fruits))  # True
# оператор is сравнивает адреса объектов в памяти а не содержимое объектов

print('fruits is other_fruits: ', fruits is other_fruits)  # False

print('\'apple\' in fruits: ', 'apple' in fruits)  # True
print('\'apple\' in other_fruits', 'apple' in other_fruits) # True
