user_data = ['Vitaliy', 23]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


my_name, my_comments_qty = user_data

print(user_info(*user_data))
print(user_info(my_name, my_comments_qty))
#  print(user_info(name = user_data[0], comments_qty = user_data[1]))

#  в случае передечи большего количества аргументов
# ValueError: too many values to unpack (expected 2)


"""
        ЗАДАНИЕ
1. Создайте список из 3-х словарей.
2. При помощи оператора распакови списков создайте три переменных
каждая из которых будет содержать один из словарей.
3. Далее создайте функцию которая будет принимать два аргумента, 
в вызове функции вы должны распаковывать словарь.
4. Функцию вызовите трижды. Укаждого из этих словарей должно быть по два ключа.
"""

my_list = [{'1': 1}, {'2': 2}, {'3': 3}]
first_dict, second_dict, third_dict = my_list


def fun_print_dict(key, val=0):
    if not val:
        return f"key is {key}"
    return f"'{key}': {val} "


print(first_dict)
print(second_dict)
print(third_dict)
