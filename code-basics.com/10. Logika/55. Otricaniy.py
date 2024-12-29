def is_even(number):
    return number % 2 == 0


print(is_even(10))      # => True
print(not is_even(10))  # => False


not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False


def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)


is_palindrome('шалаш')  # true
is_palindrome('хекслет')  # false
is_palindrome('Довод')  # true
is_palindrome('Функция')  # false

is_not_palindrome('шалаш')  # false
is_not_palindrome('Ага')  # false
is_not_palindrome('хекслет')  # true
