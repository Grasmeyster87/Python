def person_info(name, age):
    print(name, age)

# person_info("Bob", 25)

def person_info1(**args):
    print(args["name"])
    print(args.get("city", 'New York')) # из списка args (изменяется на person) выбрать ключь "city" значения по умолчанию 'New York'
    print(type(args))

person_info1(name = "Bob", age = 25)