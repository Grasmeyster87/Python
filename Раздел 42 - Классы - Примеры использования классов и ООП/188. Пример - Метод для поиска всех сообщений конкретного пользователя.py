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

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user

    def find_posts_by_author(self, author):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts


forum = Forum()
bogdan = forum.register_user('bogdan123', 'b@gmail.com')
alice = forum.register_user('alice643', 'a@a.com')

# print(forum.users)

forum.create_post("My first post", "Post content", bogdan)
# print(forum.posts)
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

# print(forum.find_user_by_username('admin12'))  # None
# print(forum.find_user_by_username('bogdan123').email)  # b@gmail.com

forum.create_post("Second great post", "Post content", bogdan)

found_posts = forum.find_posts_by_author(bogdan)

# print(found_posts)
found_posts_titles = [post.title for post in found_posts]
print(found_posts_titles)
