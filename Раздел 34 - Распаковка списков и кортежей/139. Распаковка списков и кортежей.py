# my_fruits = ['apple', 'banana', 'lime'] # list
my_fruits = ('apple', 'banana', 'lime')  # tuple

my_apple = my_fruits[0]
my_banana = my_fruits[1]
my_lime = my_fruits[2]

# my_apple,  my_banana, my_lime = my_fruits
my_apple,  *remaining_fruits = my_fruits
# print(my_apple)
# print(my_banana)
# print(my_lime)
print(remaining_fruits)
# print(type(remaining_fruits))
"""
LIST, TUPLE - упорядоченая последовательнойсть элементов
"""
