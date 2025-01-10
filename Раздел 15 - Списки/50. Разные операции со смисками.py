greeting = "Hello from Python"
greeting_letters = list(greeting)  # конвертация в список

print(greeting_letters)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)

print(my_dict_keys)

# ------ Арифметические операции в списках -----------

ratings = [2.5, 5.0, 4.3, 3.7]

print(min(ratings))
print(max(ratings))
print(sum(ratings))

print(sum(ratings) / len(ratings))

# --------- Обединение списков ------------------------

my_ratings = [2.5, 5.0]

other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print('\nall_ratings: ', all_ratings)

# --------- Нарезка списков ---------------------------

ratings = [2.5, 5.0, 4.3, 3.7, 4.5]

first_two_ratings = ratings[:2]
print('\nfirst_two_ratings: ', first_two_ratings)

middle_ratings = ratings[1:-1]
print('\nmiddle_ratings', middle_ratings)

last_two_ratings = ratings[-2:]
print('\nlast_two_ratings: ', last_two_ratings)
