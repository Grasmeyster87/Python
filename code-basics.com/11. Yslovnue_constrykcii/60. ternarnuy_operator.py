def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'


print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question


def flip_flop(string1):
    return 'flop' if string1 == 'flip' else 'flip'


print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'
