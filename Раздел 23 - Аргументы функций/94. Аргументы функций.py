def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

print(my_fn(10, 3))

def sum_nums(a, b):
    c = a + b
    return (c)

print(sum_nums(2, 5))

# print(sum_nums(2))  # TypeError: sum_nums() missing 1 required positional argument: 'b'
# print(sum_nums())  # TypeError: sum_nums() missing 2 required positional arguments: 'a' and 'b'

# print(sum_nums(2, 3, 7))  # TypeError: sum_nums() takes 2 positional arguments but 3 were given