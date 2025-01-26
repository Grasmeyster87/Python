my_number = 25

if my_number > 0:
    print(my_number, "is positive number")


person_info = {
    'age': 20,
}

if not person_info.get('name'):
    # Действия в случаях, если:
    # 1. Ключа "name" у объекта "person" нет
    # 2. Ключ "name" есть, но его значение ложно
    print("Имя отсутствует")


if 10 > 2:
    print(True)

num_one = 10
num_two = 5

if (num_one > 0 and 
    num_two > 0 and 
    isinstance(num_one, int) and 
    isinstance(num_two, int)):
    print("Both numbers are ints and positiv")