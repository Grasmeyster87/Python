a = None
b = 5
c = "a"

print(a and b and print("not called")) # если первое значение истина то проверяют следющее и выводят если оно истинно
print(bool(a and b and c))