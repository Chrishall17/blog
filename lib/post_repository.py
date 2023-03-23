from lib.post import Post

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"])
            posts.append(item)
        return posts

    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"])

    def create(self, post):
        self._connection.execute('INSERT INTO posts (title) VALUES (%s)', [
                                post.title])
        return None

    def find_by_tag(self, tag):
        rows = self._connection.execute(
            "SELECT posts.id, posts.title " \
            "FROM posts " \
            "JOIN posts_tags ON posts_tags.post_id = posts.id " \
            "JOIN tags ON posts_tags.tag_id = tags.id " \
            f"WHERE tags.name = '{tag}'")
        tag_list = []
        for row in rows:
            post = Post(row["id"], row["title"])
            tag_list.append(post)

        return tag_list
