def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки,
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i = i + 1


name = 'Arya'
# print_name_by_symbol(name)


def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i -= 1


word = 'Hexlet'

print_reversed_word_by_symbol(word)
# => 't'
# => 'e'
# => 'l'
# => 'x'
# => 'e'
# => 'H'
