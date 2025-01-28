nums = (3, 5, 10)
squares = (num * num for num in nums)

print(squares)
print(type(squares))


squares1 = (num * num for num in range(6))
print(squares1)

print(type(squares1))


for num in squares1:
    print(num)

# ---------------------------------------------

from sys import getsizeof

squares_gen = (num * num for num in range(10000))

print(getsizeof(squares_gen))

print(type(squares_gen))

squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))

print(type(squares_list))