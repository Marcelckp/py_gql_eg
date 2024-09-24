# Read me for project

Run the python virtual environment:

```bash
source env/bin/activate
```

To create the Virtual Environment we need to run the following command:

```bash
python3 -m venv env
```

To display all of the dependencies for a project. You can freeze your current virtual project environments with the following command:

```bash
pip freeze > requirements.txt
```

To run the application use the following command:

```bash
uvicorn main:app --reload
```

## Using the GQL endpoint

here is a demo query to try out when playing with the graphql endpoint

```graphql
query getAllUsers {
  users{
    id
    name
    posts {
      title
    }
  }
}
```
