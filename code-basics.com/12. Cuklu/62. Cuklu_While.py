# Напишем функцию который будет n раз выводить на экран строку 'Hello!':

def print_hello(n):
    counter = 0
    while counter < n:
        print('Hello!')
        counter = counter + 1


print_hello(2)


def print_numbers(last_number):
    # i сокращение от index (порядковый номер)
    # используется по общему соглашению во множестве языков
    # как счетчик цикла
    i = 1
    while i <= last_number:
        print(i)
        i = i + 1
    print('finished!')


print_numbers(3)
# => 1
# => 2
# => 3
# => finished!


def print_numbers(last_number):
    i = last_number
    while 0 <= i:
        print(i)
        i = i - 1
    print('finished!')


print_numbers(4)
