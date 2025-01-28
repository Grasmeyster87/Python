"""
        СОКРАЩЕННЫЙ ЦИКЛ FOR IN
Выражение for Элемент in Последовательность if Условие

"""

all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = []

# for num in all_nums:
#     absolute_nums.append(abs(num))

# absolute_nums = [abs(num) fornum in allnums]

# print(absolute_nums)

# print(all_nums)

# positive_nums = []

# for num in all_nums:
#     if num > 0:
#         positive_nums.append(num)

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)

print(all_nums)
