my_set = {'abc', 'd', 'f', 'y'}

other_set = {'abc', 'f', 'd', 'l'}

a = {'abc', 'd', 'f', 'y'}

b = {'abc', 'f', 'd', 'l'}

# copied_set = my_set.copy()
# my_set.add('t')
# copied_set.add('l')
# print(my_set & copied_set)  # пересечение множеств

# print(my_set)
# print(copied_set)


# print(my_set.symmetric_difference(copied_set))
# print(my_set & copied_set)

print(( a | b) - (a & b))
print(a.symmetric_difference(b))