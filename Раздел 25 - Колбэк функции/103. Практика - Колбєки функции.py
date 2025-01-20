# ------------------ Пример 1 -----------------------

def other_fn():
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback(other_fn)


def print_number_info(num):
    if (num % 2) == 0:
        print("Enter number is even")
    else:
        print("Entered number is odd")


def print_square_num(num):
    print("Square of the num is", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Enter any number:'))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)

# ------------------ Пример 2 -----------------------

def send_data(data):
    return {'data': 'sending data to the remote server'}
    

def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    send_data_fn(updated_data)

# process_data ('name': 'Vitaliy', send_data)
