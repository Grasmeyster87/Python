"""
РАБОТА С АРГУМЕНТАМИ ПРОГРАММЫ С ПОМОЩЬЮ МОДУЛЯ SYS
"""
import sys

print(sys.argv)

# username = sys.argv[1]
# password = sys.argv[2]
username = sys.argv[1] = 'Vitaliy'
password = sys.argv[2] = '1234'

filename, username, password = sys.argv

if len(sys.argv) < 3:
    raise IOError("You must provide username and password")

print(username, password)
