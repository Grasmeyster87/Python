{"key1": True, "key2": 10}
person = {"name": "Bogdan"}
print (person)
print(type(person))
print(person['name'])
person.get("age") # получение значения значения словаря по ключю (в случае отсутствия ничего не выводится)

str(person.get("age"))

print(person.get("age", 18)) # если в словаре нет значения age 18 значение по умолчанию
person["happy"] = True # добавление значения в словарь

print(person)

print(len(person))

print(person.keys())
print(person.values())

person["hobbies"] = ["books", "snowboarding"]
print(person)

person["hobbies"].pop()
print(person)

del person["hobbies"]
print(person)