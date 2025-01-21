a = [1, 2]
b = [1, 2]
a == b

print(a == b)  # True
print(a.__eq__(b))  # True
print(a.__eq__)  # <method-wrapper '__eq__' of list object at 0x0000000001A76040>
#  __eq__ магический метод сравнения equal

print(id(a) == id(b))  # False

print(id(a))
print(hex(id(a)))