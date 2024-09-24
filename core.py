import strawberry
from typing import List, Optional
from controller import CreateMutation, Queries
from schema import UserType, PostType, CommentsType

@strawberry.type
class Mutation:
    # temp : int = None
    add_user: UserType = strawberry.mutation(resolver=CreateMutation.add_user)
    add_post: PostType = strawberry.mutation(resolver=CreateMutation.add_post)
    add_comment: CommentsType = strawberry.mutation(resolver=CreateMutation.add_comment)

@strawberry.type
class Query:
    # temp : int = None
    list_users: List[UserType] = strawberry.field(resolver=Queries.get_all_users)
    get_user: UserType = strawberry.field(resolver=Queries.get_user)