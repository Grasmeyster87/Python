import re

test_password = 'ASDfas2345'


def check_password(password):
    # length_regexp = r"\S{8,}"
    # # проверяем количество символов в строке минимум 8,
    # \S  при этом пробелы табуляции и переходы на новую строку не считаются
    length_pattern = re.compile(r"\S{8,}")

    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    # паттерн проверяет наличие букв в нижнем регистре в пароле + 1 вхождение

    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    # паттерн проверяет наличие букв в верхнем регистре в пароле + 1 вхождение

    number_pattern = re.compile(r"^.*[0-9]+.*$")

    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")

    no_whitespace_pattern = re.compile(r"^\S*$")
    # Любые символы (\S) любое количество раз, кроме пробелов перехода на новую строку

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password")

    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")

    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")

    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")

    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbol @%#!&*^")

    return (True, "Password is valid!")


# print(check_password(test_password))

# print(check_password('asdfASD 234  !234'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('asdbADGAG'))
# print(check_password('3234sfASDF'))
# print(check_password('asdfASDF3242!&'))

while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])