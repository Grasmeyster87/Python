a = {1, 2, 3, 4, 5}
b = {5, 7, 8, 9}

a.add(0)
b.add(10)
c = a | b
print('a: ', a)
print('b: ', b)
print('a.intersection(b): ', a.intersection(b))
print('c: ', c)
print('list(c): ', list(c))