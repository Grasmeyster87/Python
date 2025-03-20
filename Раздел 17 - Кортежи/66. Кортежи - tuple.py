# Кортежи
my_fruits = ('apple', 'banana', 'lime')
print('\nlen(my_fruits): ', len(my_fruits))

posts_ids = (151, 245, 762,  167)
print('\nposts_ids[0]: ', posts_ids[0])

user_inputs = (True, 'hi', 10.5)

my_nums = (10, 5, 100, 0)

print(type(my_nums))


users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])

users[1]['user_id'] = 100

print(users[0]['user_id'])
print(users[1]['user_id'])

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruit = (my_fruit, other_fruit, new_fruit)

print(all_fruit)

internal_ids = (151, 245)
external_ids = (624, 451, 941)

all_ids = internal_ids + external_ids

print(all_ids)