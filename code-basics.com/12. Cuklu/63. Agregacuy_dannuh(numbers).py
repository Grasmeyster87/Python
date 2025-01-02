
def sum_numbers_from_range(start, finish):
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    sum = 0  # Инициализация суммы
    while i <= finish:  # Двигаемся до конца диапазона
        sum = sum + i   # Считаем сумму для каждого числа
        i = i + 1       # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    return sum


print(sum_numbers_from_range(5, 7))  # 5 + 6 + 7 = 18
sum_numbers_from_range(1, 2)  # 1 + 2 = 3

# [1, 1] диапазон с одинаковым началом и концом — тоже диапазон
# Он включает одно число — саму границу диапазона
print(sum_numbers_from_range(1, 1))      # 1
print(sum_numbers_from_range(100, 100))  # 100

print('\n')


def multiply_numbers_from_range(start, stop):
    res = start
    count = start
    while count < stop:
        count = count + 1
        res = res * count
    return res


print(multiply_numbers_from_range(1, 5))  # 1 * 2 * 3 * 4 * 5 = 120
print(multiply_numbers_from_range(2, 3))  # 2 * 3 = 6
print(multiply_numbers_from_range(6, 6))  # 6
