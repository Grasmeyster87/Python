def sum(*args):
    total = 0
    for arg in args:
        print(arg)
        total += arg
    return total

print("\nResult work fuction sum() = ", sum(5, 2, 10, 15))