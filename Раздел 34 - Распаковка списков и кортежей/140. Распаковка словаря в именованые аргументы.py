user_profile = {
    'name': 'Bogdan',
    'comments_qty': 23,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


name, comments_qty = user_profile
print(name, comments_qty)  # получаем значения ключей

print(user_info(**user_profile))
# print(user_info(user_profile['name'], user_profile['comments_qty']))
print(user_info(name=user_profile['name'],
      comments_qty=user_profile['comments_qty']))
