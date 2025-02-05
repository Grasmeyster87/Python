import re  # Regular expression

my_string = "My name is Vitaliy."
other_string = "My name is Vitaliy!"
instructor_string = "My name is Vitaliy. Vitaliy is instructor"

res = re.search(r'V.....y\.$.', my_string)

# my_pattern = re.compile(r'V.....y\.$')
my_pattern = re.compile(r'My.*\.$')
instructor_pattern = re.compile(r'V.....y')

# print(my_pattern)  # re.compile('My.*\\.$')

# <re.Match object; span=(0, 19), match='My name is Vitaliy.'>
print(my_pattern.search(my_string))
print(my_pattern.match(my_string))  # match совпадения если нет то None
print(my_pattern.match(other_string))

print(instructor_pattern.findall(instructor_string))
