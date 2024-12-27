def print_params(a=1, b=2, c=None, d=4):
    print(a, b, c, d)

# Нужно передать только d, но приходится передавать все


print_params(1, 2, 3, 8)


# Именованные аргументы позволяют передавать только d
# Для остальных аргументов используются значения по умолчанию
print_params(d=8)


def trim_and_repeat(text, offset=0, repetitions=1):
    return f'{text[offset:] * repetitions}'


text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2))  # => honhon
print(trim_and_repeat(text, repetitions=3))  # => pythonpythonpython
print(trim_and_repeat(text))  # => python
