from lib.tag import Tag

"""
Tag constructs with an id, name and author name
"""
def test_tag_constructs():
    tag = Tag(1, 'Coding')
    assert tag.id == 1
    assert tag.name == 'Coding'

"""
We can format tag to strings nicely
"""
def test_tags_format_nicely():
    tag = Tag(1, 'Coding')
    assert str(tag) == "1 - Coding"

"""
We can compare two identical tags
And have them be equal
"""
def test_tags_are_equal():
    tag1 = Tag(1, 'Coding')
    tag2 = Tag(1, 'Coding')
    assert tag1 == tag2