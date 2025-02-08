# import sys

# sys.path.append("/usr/local/lib/python3.9/site-packages")
# sys.path.append("./.venv/Lib/site-packages/requests")
import requests

my_request = requests.get('https://www.python.org')
# print(my_request)

print(my_request.text)
# print(my_request.status_code)
