def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type


print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'


number = 10

if number > 10:
    print("Number is greater than 10")
else:
    if number == 10:
        print("Number is exactly 10")
    else:
        print("Number is less than 10")


# Правильно
def check_number(number):
    if number > 0:
        print("Число положительное")
        if number > 10:
            print("Число больше 10")
    else:
        print("Число не положительное")


check_number(3)  # => Число положительное


def normalize_url(url):
    prefix = 'https://'
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == 'http://':
            return prefix + url[7:]
        else:
            return prefix + url


print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
