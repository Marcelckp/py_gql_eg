from typing import List
from models.Comment import Comment
from models.Post import Post
from models.User import User
from schema import CommentInput, CommentsType, PostInput, PostType, UserInput, UserType
class CreateMutation:
    def add_user(self, user_data: UserInput):
        #Task 13: Code Here
        return None
        
    def add_post(self, post_data: PostInput):
        #Task 14: Code Here
        return None

    def add_comment(self, comment_data: CommentInput):
        # Task 15: Code Here
        return None

# Task 16: Code Here
class Queries:
    def get_all_users(self) -> List[UserType]:
        return None
    def get_single_user(self, user_id: int) -> UserType:
        return None