def my_fn():
    pass


print(my_fn())


def my_fn1(a, b):
    a = a + 1
    c = a + b
    return c


num_one = 10
num_two = 5

res = my_fn1(num_one, num_two)
print(res)
print(num_one)
