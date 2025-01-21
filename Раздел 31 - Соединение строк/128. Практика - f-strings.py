my_name = 'Vitaliy'
my_hobby = 'running'

time = 8

# info = my_name + ' likes ' + my_hobby + ' at ' +str(time) + ' o\'clock '

info = f"{my_name} likes {my_hobby} at {str(time)} o\'clock".title()
print(info)

# .title() делает заглвной первую букву каждого слова в строке

fruit = 'apple'
two_sentense = "I love apple!"
third_sentence = "Apples are healthy!"
info1 = f" My favorite fruit is {fruit}! {two_sentense} {third_sentence}"
print(info1)
