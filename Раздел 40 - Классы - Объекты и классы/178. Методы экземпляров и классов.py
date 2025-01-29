class Comment:
    def __init__(this, text, intial_votes_qty=0):
        this.text = text
        this.votes_qty = intial_votes_qty

    def upvote(this, qty):
        # this.votes_qty += 1
        this.votes_qty += qty

    def reset_votes_qty(this):
        this.votes_qty = 0


first_comment = Comment("First comment")
second_comment = Comment("Second comment")

# <bound method Comment.upvote of <__main__.Comment object at 0x0000000001376A50>>
print(first_comment.upvote)

print(Comment.upvote)  # <function Comment.upvote at 0x0000000001633F60>

# Comment.upvote() # TypeError: Comment.upvote() missing 2 required positional arguments: 'this' and 'qty'
# Comment.upvote(first_comment)

print(Comment)

print(object)

# Проверка пренадлежности классу

print(isinstance(first_comment, Comment))
print(type(first_comment) == Comment)

print(isinstance(first_comment, object))

print(first_comment.text)
print(second_comment.text)
