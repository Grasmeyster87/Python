try:
    print('10'/0)  # unsupported operand type(s) for /: 'str' and 'int'
    print(10/0)
    # Traceback - TypeError: unsupported operand type(s) for /: 'str and 'int'
    print(10/0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(type(e))
    print(e)
    # unsupported operand type(s) for /:
    'str' and 'init'

print("Continue...")
