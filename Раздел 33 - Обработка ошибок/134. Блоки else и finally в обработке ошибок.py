try:
    print(10/5)  # 2.0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:  # выполняется если ошибок в блоке try не возникло
    print("There was no error")
finally:  # блок выполняется в любом случае
    print('Continue...')  # Continue...
