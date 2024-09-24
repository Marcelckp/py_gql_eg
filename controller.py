from typing import List
from models.Comment import Comment
from models.Post import Post
from models.User import User
from schema import CommentInput, CommentsType, PostInput, PostType, UserInput, UserType
class CreateMutation:
    def add_user(self, user_data: UserInput):
        # Validate if the user doesn't already exist
        user = User.where("email", user_data.email).get()
        if user:
            raise Exception("A user with the provided email already exists")

        # add user to db
        # Create new empty user object
        user = User()

        # Assign values to the user object
        user.name = user_data.name
        user.email = user_data.email
        user.address = user_data.address
        user.phone_number = user_data.phone_number
        user.sex = user_data.sex
        
        # Save the user object to the database and return
        user.save()
        return user
        
    def add_post(self, post_data: PostInput):
        # Get the user to relate this post to
        user = User.find(post_data.user_id)
        if not user:
            raise Exception("User not found")
        
        # Create new empty post object
        post = Post()
        
        # Assign values to the post object
        post.user_id = post_data.user_id
        post.title = post_data.title
        post.body = post_data.body

        # Save the post object to the database add this to the users object and return
        post.save()
        user.posts().attach(post)
        return post

    def add_comment(self, comment_data: CommentInput):
        # Get the user to relate this comment to
        user = User.find(comment_data.user_id)
        if not user:
            raise Exception("User not found")
        
        # Get the post to relate this comment to
        post = Post.find(comment_data.post_id)
        if not post:
            raise Exception("Post not found")
        
        # Create new empty comment object
        comment = Comment()

        # Assign values to the comment object
        comment.user_id = comment_data.user_id
        comment.post_id = comment_data.post_id
        comment.body = comment_data.body

        # Save the comment object to the database add this to the users object and add it to the post object and return
        comment.save()
        user.comments().attach(comment)
        post.comments().attach(comment)
        return comment

class Queries:
    def get_all_users(self) -> List[UserType]:
        return User.all()
    def get_user(self, user_id: int) -> UserType:
        user = User.find(user_id)
        if not user:
            raise Exception("User not found")
        return user