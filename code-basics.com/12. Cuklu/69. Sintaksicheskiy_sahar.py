def filter_string(text, char):
    string = ''
    index = 0
    while index < len(text):
        if text[index] != char:
            string = f'{string}{text[index]}'
        index += 1
    return string


text = 'If I look back I am lost'
print(filter_string(text, 'I'))  # 'f  look back  am lost'
print(filter_string(text, 'o'))  # 'If I lk back I am lst'
