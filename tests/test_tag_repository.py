from lib.tag_repository import TagRepository
from lib.tag import Tag

"""
When we call TagRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blog_posts_tags.sql") # Seed our database with some test data
    repository = TagRepository(db_connection) # Create a new TagRepository

    tags = repository.all() 

    assert tags == [
        Tag(1, 'coding'),
        Tag(2, 'travel'),
        Tag(3, 'cooking'),
        Tag(4, 'education')
    ]

"""
When we call TagRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    tag = repository.find(1)
    assert tag == Tag(1, 'coding')

"""
When we call TagRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    repository.create(Tag(None, "lifestyle"))

    result = repository.all()
    assert result == [
        Tag(1, 'coding'),
        Tag(2, 'travel'),
        Tag(3, 'cooking'),
        Tag(4, 'education'),
        Tag(5, 'lifestyle')
    ]

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    result = repository.find_by_post(1)
    assert result == [
        Tag(1, 'coding')
    ]