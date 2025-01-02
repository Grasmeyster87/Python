for i in range(1, 4):
    print(i)

# => 1
# => 2
# => 3


for i in range(3, 0, -1):
    print(i)

# => 3
# => 2
# => 1


def print_table_of_squares(first, last):
    for i in range(first, last + 1):
        print(f'square of {i} is {i**2}')


print_table_of_squares(1, 3)
# => square of 1 is 1
# => square of 2 is 4
# => square of 3 is 9
