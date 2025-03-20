def get_posts_info(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )
    return info


info = get_posts_info(name='Bogdan', posts_qty=25, id=1351)
print(info)
