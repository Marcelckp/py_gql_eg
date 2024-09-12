import strawberry
from typing import List, Optional
from controller import CreateMutation, Queries
from schema import UserType, PostType, CommentsType

@strawberry.type
class Mutation:
    temp : int = None
@strawberry.type
class Query:
    temp : int = None