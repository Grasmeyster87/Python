try:
    print(10/0)  
    print('10'/0)  
except ZeroDivisionError as e:
    # print(isinstance(e, Exception))
    # print(isinstance(e, object))
    print(e)
except TypeError as e:
    print(e)


"""
try:
    print(10/0)  # 2.0
except Exception as e:
    print(e)

try:
    print(10/0)  # 2.0
except: # не рекомендуется !!!
    print("Some error occurred")
"""
