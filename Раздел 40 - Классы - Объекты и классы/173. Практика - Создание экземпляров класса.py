class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()

# print(my_car)
# print(type(my_car))
# print('isinstance(my_car, Car): ', isinstance(my_car, Car))
# print('isinstance(my_car, object): ', isinstance(my_car, object))

# print('\n')

# print(dir(my_car))

# print('\n')
# print(my_car.__dict__)

# my_car.move()
# my_car.stop()

my_second_car = Car()

# print('my_car == my_second_car: ', my_car == my_second_car)
# print('id(my_car): ', id(my_car), 'id(my_second_car): ', id(my_second_car))

Car.move(my_car)