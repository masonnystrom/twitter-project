# twitter-project
Project for creating a web app


## Installation


## Setup

Migrate the DB: 
```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
```

## Usage

```sh
# Mac:
FLASK_APP=web_app flask run

# Windows:
set FLASK_APP=web_app # one-time thing, to set the env var
flask run
```