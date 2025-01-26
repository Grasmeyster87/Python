# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Один из аргументов не целое число"

#     if a >= b:
#         return f"{a} больше или равно {b}"

#     return f"{a} меньше {b}"


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Один из аргументов не целое число"
    elif a >= b:
        info = f"{a} больше или равно {b}"
    else:
        info = f"{a} меньше {b}"
    return info


print(nums_info(True, 10))
# Один из аргументов не целове число
print(nums_info(10, 2))
print(nums_info(4, 15))
