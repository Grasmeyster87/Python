def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].lower() == char.lower():
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count


print(count_chars('HexlEt', 'e'))  # 2
print(count_chars('HexlEt', 'E'))  # 2
