
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        res = num1/num2
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(res)

    continue_to_do = input("You want to continue? y/n: ")
    if continue_to_do == 'n':
        break
