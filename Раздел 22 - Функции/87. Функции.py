"""
Функция - блок кода который множно ввыполнять многократно с изменяемыми параметрами
"""

def sum(a, b):
    c = a + b
    print(c)

a = 5
b = 3
sum(a, b)

a = 8
b = 12

sum(a, b)
print(type(sum))

def my_fn(a, b):
    a = a + 1
    c = a + b
    return c  # в случае отсутствия return возврат None

res = my_fn(10, 3)
print(res)

