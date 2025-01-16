"""
ДИАПАЗОН - упорядоченая не изменяемая последовательность елементов
            обычно используются в цыклах
"""
my_range = range(7)
my_range1 = range(10, 20, 3)

# print(type(my_range))  # <class 'range'>
# print(my_range)  # range(0, 7)
# print(list(my_range))  # [0, 1, 2, 3, 4, 5, 6]

print(my_range1)
print(list(my_range1))

print(my_range1[0])
print(my_range1[1])
print(my_range1[2])
print(my_range1[3])
# print(my_range1[4])

for n in my_range:
    print(n)
