def is_arguments_for_substr_correct(text, index, long):
    if long < 0:
        return False
    elif index < 0:
        return False
    elif index > len(text) - 1:
        return False
    elif (index + long > len(text)):
        return False
    return True


string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True
