class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        return post


forum = Forum()
bogdan = forum.register_user('bogdan123', 'b@gmail.com')
alice = forum.register_user('alice643', 'a@a.com')

# print(forum.users)

forum.create_post("My first post", "Post content", bogdan)
# print(forum.posts)
print(forum.posts[0].title)
print(forum.posts[0].content)
print(forum.posts[0].author.username)
print(forum.posts[0].author.email)