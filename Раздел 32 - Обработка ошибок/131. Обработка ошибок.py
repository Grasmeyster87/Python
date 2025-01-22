

try:
    print(10/0)  # ZeroDivisionError: division by zero
    # print(10 + '1')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
except ZeroDivisionError:
    print(ZeroDivisionError)  # <class 'ZeroDivisionError'>
    print('Error - Division by zero!')

print('Continue...')
