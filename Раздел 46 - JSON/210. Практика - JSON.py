import json

json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'
json_array = '[{"1": 1}, {"b": 2}]'

try:
    sneakers = json.loads(json_str)
    json_from_dict = json.dumps(sneakers, indent=1)
    print(json_from_dict)
    print('type(sneakers)', type(sneakers))
    print('type(json_from_dict)', type(json_from_dict))

    print(sneakers['brand'])
    print(sneakers['qty'])
    print(sneakers['status']['isForSale'])
    print(sneakers)

    my_list = json.loads(json_array)
    print(my_list)
except Exception as e:
    print(repr(e))
