from lib.tag import Tag

class TagRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from tags')
        tags = []
        for row in rows:
            item = Tag(row["id"], row["name"])
            tags.append(item)
        return tags

    def find(self, tag_id):
        rows = self._connection.execute(
            'SELECT * from tags WHERE id = %s', [tag_id])
        row = rows[0]
        return Tag(row["id"], row["name"])

    def create(self, tag):
        self._connection.execute('INSERT INTO tags (name) VALUES (%s)', [
                                tag.name])
        return None

    def find_by_post(self, post_id):
        rows = self._connection.execute(
            "SELECT tags.id, tags.name " \
            "FROM tags " \
            "JOIN posts_tags ON posts_tags.tag_id = tags.id " \
            "JOIN posts ON posts_tags.post_id = posts.id " \
            f"WHERE posts.id = '{post_id}'")
        tag_list = []
        for row in rows:
            tag = Tag(row["id"], row["name"])
            tag_list.append(tag)

        return tag_list
