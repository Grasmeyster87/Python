import random

print(random.random())  # генерация случайного числа
# генерация случайного числа типа int оба числа входят в диапазон

print(random.randint(1, 10))
# выбор случайного элемента с последовательности

print(random.choice('abcdasdafsdfasdfsdf'))
# выбор случайного элемента с последовательности

# выборка с диапазона значений 2-х элементов
print(random.choices([1, 10, 4, 3, 34, 56, 45, 34], k=2))

my_list_shuffle = [1, 10, 4, 3, 34, 56, 45, 34]
print(random.shuffle(my_list_shuffle))  # мутирует элементы последовательности
print(my_list_shuffle)
random.shuffle(my_list_shuffle)
print(my_list_shuffle)

# Генерируем Пароль

print('\nГенерируем Пароль: ', ''.join(random.choices(
    '0123456789FBCDIFGHIGKLMNOP_-*/', k=20)))  # генерируется на основе seed value на основе текущей даты
