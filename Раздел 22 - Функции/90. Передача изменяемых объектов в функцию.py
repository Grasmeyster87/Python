def increase_person_age(person):
    print(id(person_one))
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21
}

print(id(person_one))

increase_person_age(person_one)
print(person_one['age'])

"""
ВНУТРИ ФУНКЦИИ НЕ РЕКОМЕНДУЕТСЯ МЕНЯТЬ ВНЕШНИЕ ОБЪЕКТЫ !!!
"""
