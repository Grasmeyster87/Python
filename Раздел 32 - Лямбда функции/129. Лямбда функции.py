"""
ЛЯМБДА ФУНКЦИИ
"""


def mult(a, b):
    return a * b


print(mult(10, 5))


def mult1(a, b): return a * b
lambda a, b : a * b

print(mult1(10, 5))

# -------------------------------------------------------
def greeting(greet):
    return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good Morning")

print(morning_greeting('Vitaliy'))

evening_greeting = greeting("Good Evening")

print(evening_greeting('Vitaliy'))
