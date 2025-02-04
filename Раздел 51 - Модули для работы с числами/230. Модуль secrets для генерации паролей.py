import secrets
import string

# ----------------- Генерация случайных паролей ---------------------
# print('\nstring.ascii_letters', string.ascii_letters)
# # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# print('\nstring.ascii_lowercase', string.ascii_lowercase)
# # abcdefghijklmnopqrstuvwxyz

# print('\nstring.ascii_uppercase', string.ascii_uppercase)
# # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# print('\nstring.digits', string.digits)
# # 0123456789

# print('\nstring.ascii_letters + string.digits',
#       string.ascii_letters + string.digits)

# print('\nstring.punctuation', string.punctuation)
# # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# print('\nstring.ascii_letters + string.digits + string.punctuation',
#       string.ascii_letters + string.digits + string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation

print(''.join(secrets.choice(all_chars) for i in  range(200)))