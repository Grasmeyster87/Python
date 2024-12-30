"""Рассмотрим функцию, которая определяет тип переданного предложения:"""


def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'quastion'
    return 'normal'


print(get_type_of_sentence('Hodor'))
print(get_type_of_sentence('Hodor?'))

""" if a == 42:
      # отступ и начало блока if
        # все строки кода с одним отступом выполняются в одном блоке
        print('First')
        print('Second')
# конец отступа и выход из блока
print('Goodbye!')
"""


def guess_number(num):
    if num == 42:
        return 'You win!'
    return 'Try again!'


print(guess_number(42))  # You win!
print(guess_number(61))  # Try again!
