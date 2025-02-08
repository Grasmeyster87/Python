
# print('Hello World from Python!!! \n')

# print('Hello Vitaliy')

# print(2+2)


# def print_hi(name):
#     print(f'Hi, {name}')


# if __name__ == '__main__':
#     print_hi('PyCharm')
#     # 111

import requests

my_request = requests.get('https://www.python.org')
print(my_request)

# pipenv install autopep8

print(my_request.text)
print(my_request.status_code)