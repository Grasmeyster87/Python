class Comment:
    def __init__(this, text, intial_votes_qty=0):
        this.text = text
        this.votes_qty = intial_votes_qty

    def upvote(this, qty):
        # this.votes_qty += 1
        this.votes_qty += qty

    def reset_votes_qty(this):
        this.votes_qty = 0


my_comment = Comment("My comment")

# print(my_comment)
# print(type(my_comment))
# print(my_comment.__dict__)
# print(dir(my_comment))
# print(my_comment.text)
# print(my_comment.votes_qty)

# my_comment.upvote(5)

# print(my_comment.votes_qty)

# my_comment.upvote(10)

# print(my_comment.votes_qty)

# ----------------------------------
# my_comment.upvote = 10
# my_comment.upvote()
print(my_comment.__dict__)
second_comment = Comment("Second comment")

second_comment.upvote(2)

print(second_comment.votes_qty)

print(my_comment.votes_qty)

my_comment.upvote(10)
my_comment.upvote(20)

print('my_comment.votes_qty: ', my_comment.votes_qty)

my_comment.reset_votes_qty()
print('my_comment.votes_qty: ', my_comment.votes_qty)
