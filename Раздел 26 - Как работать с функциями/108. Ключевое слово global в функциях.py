a = 9

def my_fn():
    global a
    a = 10

my_fn()
print(a)