"""
ОПЕРАТОК РАСПАКОВКИ СЛОВАРЯ

"""

grey_button = {
    'width': 200,
    'text': 'Buy',
    'color': 'grey'
}

red_button = {
    **grey_button,
    'color': 'red',
}

print(red_button)

print(grey_button)
