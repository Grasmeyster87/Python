button_default = {
    'text': 'Ok',
    'color': 'black',
    'width': 0,
    'height': 0,
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300,
}

button = {
    **button_default,
    **button_style,
}

button1 = button_default | button_style

print(button)
print(button1)

"""
Задание
"""

dict1 = {'1': '1'}
dict2 = {'2': '2'}
dict3 = {'3': '3'}

dict_value = (dict1 | dict2 | dict3)
print(dict_value)
