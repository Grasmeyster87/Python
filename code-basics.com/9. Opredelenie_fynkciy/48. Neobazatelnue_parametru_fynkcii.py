def my_print(text='nothing'):
    print(text)


my_print()  # => "nothing"
my_print("Hexlet")  # => "Hexlet"


def get_hidden_card(number, stars=4):
    print(f'{"*" * stars}{number[12:]}')
    return f'{"*" * stars}{number[12:]}'

# Кредитка передается внутрь как строка
# Второй параметр не передается, значит звездочек будет 4


get_hidden_card('1234567812345678')  # ****5678
get_hidden_card('1234567812345678', 2)  # **5678
get_hidden_card('1234567812345678', 3)  # ***5678


# Или используя переменные

card_number = '2034399002121100'
get_hidden_card(card_number)  # ****1100
get_hidden_card(card_number, 1)  # *1100
