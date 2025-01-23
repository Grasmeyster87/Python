
def image_info(my_dict):
    if ('image_id' not in my_dict) or ('image_title' not in my_dict):
        raise TypeError("Keys image_id and image_title must be present")
    return f"Image '{my_dict['image_title']}' has id {my_dict['image_id']}"


print(image_info({'image_title': 'My cat', 'image_id': 123}))
# TypeError: Keys image_id and image_title must be present
# print(image_info({'image_title': 'My cat', }))

try:
    print(image_info({'image_id': 123}))
except TypeError as e:
    print(e)
