my_img = ('1920', '1080')

info = (f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else ("Incorrect image formatting")

# print(info)

"""
        ЗАДАНИЕ
1. Переписать пример при помощи операторов if else

2. Используя тернарный оператор написать выражение 
проверки строки до 79 знаков \"String is short\" больше 
\"String is long\"

"""

# if len(my_img) == 2:
#     print(f"{my_img[0]}x{my_img[1]}")
# else:
#     print("Incorrect image formatting")

str = 'This string short!'

print("String is short" if len(str) < 79 else "Incorrect image formatting")
