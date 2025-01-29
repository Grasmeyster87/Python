class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1


"""
СОБСТВЕННЫЕ АТРИБУТЫ ЭКЗЕМПЛЯРОВ ОПРЕДЕЛЯЮТСЯ С 
ПОМОЩЬЮ ФУНКЦИИ  __init__
"""

"""
СОЗДАНИЕ ЭКЗЕПЛЯРА КЛАССА  COMMENT
"""

first_comment = Comment("First comment")

print(first_comment.__dict__)  # словарь собственных атрибутов

print(first_comment.text)

print(first_comment.votes_qty)

print('\n', dir(first_comment))
