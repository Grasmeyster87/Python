def count_items(count):
    # Объявляем переменную
    result = ''

    # Заполняем
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = None

    # Возвращаем
    return result


def count_items1(count):
    match count:
        case 1:
            return 'one'
        case 2:
            return 'two'
        case _:
            return None


def get_number_explanation(num1):
    match num1:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'


print(get_number_explanation(8))  # just a number
print(get_number_explanation(666))  # devil number
print(get_number_explanation(42))  # answer for everything
print(get_number_explanation(7))  # prime number
