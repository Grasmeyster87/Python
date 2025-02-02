
import json
my_test_dict = {"one": 1, "two": (1, 2, 3), "three":{"3": [1, 2, 3]}}

json_from_dict = json.dumps(my_test_dict, indent=1)

print(json_from_dict)
print(type(my_test_dict))
print(type(json_from_dict))

conver_json = json.loads(json_from_dict)
print(conver_json)