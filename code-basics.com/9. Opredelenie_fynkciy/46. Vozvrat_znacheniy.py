def greeting():
    return 'Hello, Hexlet!'


message = greeting()

print(message)  # => Hello, Hexlet

# Любой код после return не выполняется:


def greeting_with_code_after_return():
    return 'Hello, Hexlet!'
    print('Я никогда не выполнюсь')


def greeting_with_return_and_printing():
    print('Я появлюсь в консоли')
    return 'Hello, Hexlet!'


# И напечатает текст на экран, и вернет значение
message = greeting_with_return_and_printing()


def greeting():
    message = 'Hello, Hexlet!'
    return message


def double_five():
    # или return 5 + 5
    result = 5 + 5
    return result

# Определение


def run():
    return 5
    return 10


# Что будет выведено на экран?
print(run())


def say_hurray_three_times():
    return 'hurray! hurray! hurray!'


hurray = say_hurray_three_times()
print(hurray)  # => hurray! hurray! hurray!
