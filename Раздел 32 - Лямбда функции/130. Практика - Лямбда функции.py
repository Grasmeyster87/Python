def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")

print(morning_greeting('Vitaliy'))

evening_greeting = greeting("Good Evening")

print(evening_greeting('Vitaliy'))
