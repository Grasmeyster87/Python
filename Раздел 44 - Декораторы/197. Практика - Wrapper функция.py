def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):

        # Some actions before execution of the oroginal_fn
        print("\nExecuted before function")

        result = original_fn(*args, **kwargs)

        print("Function result: ", result)

        # Some actions after execution of the oroginal_fn
        print("\nExecuted after function")

        return result

    return wrapper_function


@decorator_function
def my_function(a, b):
    print("\nThis is my function!")
    return (a, b)


result = my_function(100, 50)
print(result)