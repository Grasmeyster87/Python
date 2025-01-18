def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


res = merge_lists_to_dict(list_one = ['John', 'Frank', 'Tom'], list_two = [1, 2, 3])
# print(res)

res1 = merge_lists_to_dict( ['John', 'Frank', 'Tom'], list_two = [1, 2, 3])
# print(res1)

def update_car_info(**car):    
    car['is_available'] = True
    return car

print(update_car_info( brand = 'Audy', price = 10_000 ))