def sum_nums(*args):
    print(args)  # (2, 3, 7)
    print(type(args))  # <class 'tuple'>
    # print(args[0])  # 2
    return sum(args)

print(sum_nums(2, 3, 7))  # 12
print(sum_nums())  # 0

def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info

info = get_posts_info('Bogdan', 25)
print(info)  # Bogdan wrote 25 posts
