""" Post Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Post(Model):
    """Post Model"""

    # The has many is defining the relationship between the Post and the User model where the user_id in the Post model is the foreign key that references the id in the User model that the post is associated with
    @has_many("id", "user_id")
    def posts(self):
        from .Post import Post
        return Post
    
    @has_many("id", "user_id")
    def comments(self):
        from .Comment import Comment
        return Comment