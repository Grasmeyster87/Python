from copy import deepcopy  # библиотека для полного копирования

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': [],
}

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great course!')

print(info)
print(info_deepcopy)
