import json

json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'


try:
    sneakers = json.loads(json_str)

    print(type(sneakers))

    print(sneakers['brand'])
    print(sneakers['qty'])
    print(sneakers['status']['isForSale'])
except Exception as e:
    print(repr(e))

print('\n', dir(json), '\n')
print(sneakers)

# sneakers_dumps = json.dumps(sneakers)
# отформатированый json с добавленными отступами
sneakers_dumps = json.dumps(sneakers, indent=1)

print(sneakers_dumps)

"""

КОНВЕРТАЦИЯ ТИПОВ PYTHON В ТИПЫ JSON

Python  JSON
str     String
int     Number
float   Number
True    true
False   false
None    null
dict    Object
list    Array
tuple   Array

"""
