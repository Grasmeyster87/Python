def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(3))


def is_first_letter_an_a(string):
    first_letter = string[0]
    return first_letter == 'a'


print(is_first_letter_an_a('orange'))  # => False
print(is_first_letter_an_a('apple'))   # => True


def is_international_phone(number):
    return number[0] == '+'


is_international_phone('89602223423')  # False
is_international_phone('+79602223423')  # True
