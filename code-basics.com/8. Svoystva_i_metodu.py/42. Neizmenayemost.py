name = 'Tirion'
print(name.upper())  # => TIRION
# Что напечатает на экран этот вызов?
print(name)  # => ?

name = 'Tirion'
name = name.upper()
print(name)  # => TIRIO

first_name = '  Grigor   \n'

# BEGIN (write your solution here)
first_name = first_name.strip()
print(first_name)
# END