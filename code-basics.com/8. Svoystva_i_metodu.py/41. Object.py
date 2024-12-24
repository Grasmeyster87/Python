# Подсчет длины с помощью функции len()
name = 'Hexlet'
len(name)  # 6

upper_name = name.upper()
print(upper_name) # =>  'Hellet'

print("Hexlet".upper())

name = 'Python'
name.find('t')
name.lower()

res1 = name.replace('on', 'off')
print(res1)

x = -5
# Возвращает модуль числа
# Имя выглядит странно, но это действительно имя метода
print(x.__abs__())

print(len.__doc__) # 'Return the number of items in a container.'

text = 'a MIND needs Books as a Sword needS a WHETSTONE.'

# BEGIN (write your solution here)
print(text.lower())
# END
