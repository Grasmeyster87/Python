my_cars = ['BMW', 'Mersedes']

# copied_cars = my_cars # Создание второй ссылки на список
# copied_cars = my_cars[:] # Создание копии списка
copied_cars = my_cars.copy() # Создание копии списка

copied_cars.append('Audi')

print(copied_cars)

print(my_cars)

print(id(my_cars) == id(copied_cars))