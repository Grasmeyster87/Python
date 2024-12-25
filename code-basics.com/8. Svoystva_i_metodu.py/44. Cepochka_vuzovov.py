name = 'Tirion'
print(name.upper().lower())  # => `tirion`


name = 'Tirion'
print(name.replace('Ti', 'Ki').lower())  # => ?

name = 'Tirion'
# Чему равен результат такого вызова?
print(name[1:5].upper().find('I'))


text = 'When \t\n you play a \t\n game of thrones you win or you die.'

# BEGIN (write your solution here)
text1 = text[5:15]
text2 = len(text1.strip())
print(len(text[5:15].strip()))
# END
