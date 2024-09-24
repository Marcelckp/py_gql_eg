import strawberry
from fastapi import FastAPI
from core import Mutation, Query
from strawberry.fastapi import GraphQLRouter

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema)

# Create fast api application
app = FastAPI()

# This will add the graphql app to the main app as a route /graphql with the following methods ['GET', 'POST']
# This is an alternative to the @app.get("/graphql") and @app.post("/graphql") decorators respectively
app.include_router(graphql_app, prefix="/graphql")

@app.get("/health")
def read_root():
    return {"Looking": "Good"}

@app.get("/demo")
def ping():
    return {"Test": "Response"}