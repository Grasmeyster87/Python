def my_name():
    pass
    

def my_name1():    
    return 10

def my_name2(name):    
    return name

def my_name3(name = 'Bob'):    
    return name

def my_name4(name = 'Bob'):  
    print("\n\nName value is - ", name)  
    return name.upper()

print(my_name()) # None

print(my_name1()) # 10

print(my_name2("Vitaliy")) # name

print(my_name3())

print(my_name4())