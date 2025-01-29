class Comment:
    def __init__(this, text):
        this.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

    @staticmethod
    def multiplication(val1, val2):
        return val1 * val2


first_comment = Comment("First comment")
second_comment = Comment("Second comment")
my_comment = Comment("My comment")

m_1 = Comment.merge_comments("Thanks!", "Excellent.")
print(m_1)

m_2 = my_comment.merge_comments("Great", "OK")
print(m_2)

"""
СТАТИЧЕСКИЕ МЕТОДЫ ДОСТУПНЫ КАК АТРИБУТЫ КЛАССА И КАК АТРИБУТЫ ЭКЗЕМПЛЯРА КЛАССА
"""
print("first_comment.multiplication(12, 12): ",
      first_comment.multiplication(12, 12))
print("Comment.multiplication(12, 12): ", Comment.multiplication(12, 12))
