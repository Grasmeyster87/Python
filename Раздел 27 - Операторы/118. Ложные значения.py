"""
ЛОЖНЫЕ ЗНАЧЕНИЯ - значения, которые при приведении к логическому типу даёт FALSE,
является ложным.(True - правдивым)
int 0 False
float 0.0 False
complex 0j False
dict{} False
list[] False
tuple() False
set set() False
range range (0)
str ""  ложными являются все пустые последовательности 
"""

print(bool(0))
print(bool(0.0))
print(bool(0j))


print(bool(None))

print(bool({}))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(range(0)))
print('bool((''))', bool(('')))
print(not not {})
print(not not {'a': 10})

my_list = [1, 2]

if len(my_list) > 0:
    print("List has elements")

if my_list:
    print("List has elements")