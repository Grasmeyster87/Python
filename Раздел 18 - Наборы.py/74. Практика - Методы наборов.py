my_set = {'abc', 'd', 'f', 'y'}

other_set = {'a', 'f', 'd'}

# print(my_set.intersection(other_set))
# print(my_set.intersection('abcd'))
# print(other_set.intersection(my_set))

# print(my_set.union(other_set))

# print(other_set.issubset(my_set))  # other_set не является подмножеством my_set

# print(my_set.issuperset(other_set))

# print('my_set.difference(other_set): ', my_set.difference(other_set))
# print(my_set & other_set)  # intersection
# print(my_set | other_set)  # union

# print(my_set.discard('d'))  # удаление елемента из множества
# print(my_set.remove('f'))  # This method is different from the discard() method, because the remove() method will raise an error 
# if the specified item does not exist, and the discard() method will not.
# print(my_set)

copied_set = my_set.copy()
my_set.add('t')
copied_set.add('l')
print(my_set & copied_set) # пересечение множеств

print(my_set)
print(copied_set)