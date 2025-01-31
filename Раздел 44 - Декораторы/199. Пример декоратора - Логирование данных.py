def log_function_call(fn):
    def wrapper(*args, **kwargs):
        # fn.__name__ магически атрибут с помощью которого можно получить доступ к имени функции
        print(f"\nFunction name: {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result: {result}")
        return result
    return wrapper


@log_function_call
def mult(a, b):
    return a * b


print(mult(5, 2))  # *args
# Function name: mult
# Function arguments: (5, 2), {}
# Function result: 10
# 10


print(mult(a=5, b=2))  # **kwargs
# Function name: mult
# Function arguments: (), {'a': 5, 'b': 2}
# Function result: 10
# 10


@log_function_call
def sum(a, b):
    return a + b

print(sum(40.3, 20.7))
# Function name: sum
# Function arguments: (40.3, 20.7), {}
# Function result: 61.0