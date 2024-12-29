"""

    < — меньше
    <= — меньше или равно
    > — больше
    >= — больше или равно
    == — равно
    != — не равно

"""

result = 5 > 4
print(result)  # => True
print('one' != 'one')  # => False


def is_infant(age):
    return age < 1


print(is_infant(3))  # => False


print(is_infant(0.5))  # => True


def is_pensioner(age) -> bool:
    return age >= 60


print('\n\n ----')

print(is_pensioner(75))  # True
print(is_pensioner(18))  # False
