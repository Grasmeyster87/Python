import re  # Regular expression

my_string = "My name is Vitaliy."

res = re.search('Vitaliy.', my_string)

res1 = re.search('V.....y.', my_string)
# .. одна точка один символ

res2 = re.search('V.....y.$', my_string)
# $ знак доллара искать слово в конце строки


res3 = re.search('^M.*name', my_string)
# ^ - каретка начало строки * - звездочка вс'


res4 = re.search(r'V.....y\.', my_string)
# \. обратный слешь экранировать точку для поиска
# именно точки а не символа что она обозначает в регулярных выражениях

print(res)
print(res1)
print(res2)
print(res3)
print(res4)

print(r'V.....y\n.$') # r'' - строки для вывода спец символов

print(res.span()) # вывод результата в кортеже
print(res.start()) # число начала вывода искомой фразы
print(res.end()) # число конца вывода искомой фразы