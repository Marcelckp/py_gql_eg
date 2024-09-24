#!/bin/bash

# Build the Docker image
docker build -t python_graphql_example .

# Check if the container name is already in use
if [ "$(docker ps -aqf "name=py-gql-eg")" ]; then
    echo "The container name is already in use. Deleting the container..."
    docker rm -f py-gql-eg
    echo "Container deleted. Rerunning the command..."
    docker run --name py-gql-eg -d -p 8080:8000 python_graphql_example
else
    echo "Running the Docker container..."
    docker run --name py-gql-eg -d -p 8080:8000 python_graphql_example
fi