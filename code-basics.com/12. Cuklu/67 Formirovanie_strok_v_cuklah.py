def my_substr(string, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string


string = 'If I look back I am lost'
print(my_substr(string, 1))  # => 'I'
print(my_substr(string, 7))  # => 'If I lo'
