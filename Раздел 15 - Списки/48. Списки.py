my_fruit = ['apple', 'banana', 'lime']
other_fruit = ['banana', 'apple', 'lime']
print('\nmy_fruit == other_fruit: ', my_fruit == other_fruit)
print('\nlen(my_fruit): ', len(my_fruit))

post_ids = [151, 245, 762, 167]
print('\nlen(post_ids): ', len(post_ids))

user_inputs = [True, 'hi!', '😊', 10.5]
print('\nlen(user_inputs): ', len(user_inputs))

post_ids[0] = 555
post_ids[2] = 333
print('\npost_ids: ', post_ids)

del post_ids[-1]
print('\npost_ids: ', post_ids)

users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]
print('\nlen(users): ', len(users))

print('\nusers[1][\'user_id\']: ', users[1]['user_id'])

# --------------- Переменные при формировании списков ---------------

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]
print('\nall_fruits: ', all_fruits)

# post_id = [151, 245, 762, 167]
# print(post_id[10])
