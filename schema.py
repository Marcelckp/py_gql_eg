import strawberry
from typing import List, Optional
# Task 10 - Code Here
@strawberry.type
class CommentsType:
    id: None

@strawberry.type
class PostType:
    id: None

@strawberry.type
class UserType:
    id: None

# Task 11 - Code Here
@strawberry.input
class UserInput:
    id: None

@strawberry.input
class PostInput:
    id: None

@strawberry.input
class CommentInput:
    id: None