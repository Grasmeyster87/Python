text = 'code'
for symbol in text:
    print(symbol)

# => c
# => o
# => d
# => e


def reverse_string(text):
    # Начальное значение
    result = ''
    # char - переменная, в которую записывается текущий символ
    for char in text:
        # Соединяем в обратном порядке
        result = char + result
    # Цикл заканчивается, когда пройдена вся строка
    return result


print(reverse_string('go!'))  # => '!og'


# text - произвольный текст
# char - символ, который нужно учитывать
def chars_count(text, char):
    # Так как ищем сумму, то начальное значение 0
    result = 0
    for current_char in text:
        # приводим все к нижнему регистру,
        # чтобы не зависеть от текущего регистра
        if current_char.lower() == char.lower():
            result += 1
    return result


chars_count('hexlet!', 'e')  # 2
chars_count('hExlet!', 'e')  # 2
chars_count('hExlet!', 'E')  # 2

chars_count('hexlet!', 'a')  # 0


def filter_string(text, char):
    res = ''
    for char1 in text:
        if char.lower() != char1.lower():
            res = f'{res}{char1}'
    return res


text = 'If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'
