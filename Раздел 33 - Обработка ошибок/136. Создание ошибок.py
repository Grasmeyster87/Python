def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b 

try:
    divide_nums(10, 0)
except Exception as e:  #  TypeError  ValueError
    print(e)
print('Continue...')