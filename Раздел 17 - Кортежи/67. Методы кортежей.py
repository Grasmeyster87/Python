post_ids = (151, 245, 762, 245)

print(post_ids.count(245))  # подсчет количества элементов в кортеже

print(post_ids.count(151))

print('post_ids.index(245): ', post_ids.index(245)) # получение индекса указанного значения в кортеже

print('post_ids.index(762): ', post_ids.index(762))

posts_ids = (151, 245)

posts_ids_list = list(posts_ids)
posts_ids_list.append(351)

print(posts_ids_list)
posts_ids_tuple = tuple(posts_ids_list)

print(posts_ids_tuple)
