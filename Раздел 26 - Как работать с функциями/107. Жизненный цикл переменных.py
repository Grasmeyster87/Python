"""
Жизненный цикл переменных
"""

a = 10


def my_fn():
    a = True
    b = 15
    print(a)
    print(b)


my_fn()

print(a)
# print(b)

a1 = 11


def my_fn1():
    def inner_fn():
        print('a1 = ', a1)
    inner_fn()


my_fn1()
