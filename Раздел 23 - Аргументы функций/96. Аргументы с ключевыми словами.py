def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty}"
    return info

info = get_posts_info(name = 'Bogdan', posts_qty = 25)
print(info)