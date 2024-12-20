dollars_count = 50 * 1.25
print(dollars_count)  # => 62.5

who = "dragon's " + 'mother'
print(who)

yuans_per_dollar = 6.91
dollars_count = 50 * 1.25  # 62.5
yuans_count = dollars_count * yuans_per_dollar  # 431.875

# Функция str() превращает число в строку.
# О таких превращениях будет отдельный урок.
print('The price is ' + str(yuans_count) + ' yuans')
# => The price is 431.875 yuans

euros_count = 100
dollars_count = euros_count * 1.25
print(dollars_count)
yuans_count = dollars_count * 6.91
print(yuans_count)
