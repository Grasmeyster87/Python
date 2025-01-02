def repeat(text, times):
    # Нейтральный элемент для строк — пустая строка
    result = ''
    i = 1

    while i <= times:
        # Каждый раз добавляем строку к результату
        result = result + text
        i = i + 1

    return result


print(repeat('hexlet', 3))  # 'hexlethexlethexlet'


def join_numbers_from_range(start, end):
    i = start
    result = ''
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result


join_numbers_from_range(1, 1)   # '1'
join_numbers_from_range(2, 3)   # '23'
print(join_numbers_from_range(5, 10))  # '5678910'
