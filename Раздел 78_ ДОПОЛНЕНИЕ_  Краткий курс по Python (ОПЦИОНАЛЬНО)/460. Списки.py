a = []
print (type (a))

a.append(2)
print(a)

a.append("abc")
print(a)

a.append(True)
print(a)
print(len(a)) # количество елементов

print(a[-1])

a.pop()
print(a)

a.clear()
del a