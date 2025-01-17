from copy import deepcopy  # библиотека для полного копирования

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': [],
}

# info_deepcopy = deepcopy(info)  # глубокое копирование в том числе и вложенных объектов
info_shallow_copy = info.copy()  # копирование только первого уровня
#info_deepcopy['reviews'].append('Great course!')
info_shallow_copy['reviews'].append('Great course!')
# info_deepcopy['reviews'].append('Super!')
info_shallow_copy['reviews'].append('Super!')
info['reviews'].append('Super!')

print(info)
# print(info_deepcopy)
print(info_shallow_copy)
