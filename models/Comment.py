""" Comment Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Comment(Model):
    """Comment Model"""

    # The has many is defining the relationship between the Comment and the Post model where the post_id in the Comment model is the foreign key that references the id in the Post model that the comment is associated with
    @has_many("id", "post_id")
    def comments(self):
        from .Comment import Comment
        return Comment
