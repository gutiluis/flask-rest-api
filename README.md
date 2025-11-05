# REST API
# how to run:
- python3 -m venv venv
- source venv/bin/activate

# install dependencies
- pip install -r requirements.txt

# setup database
# run the init-db command to make an instance folder and initialize the sqlitedb from the schema.sql file
flask --app flask_test_dir init-db


## Features
- SQLite database integration
- Application factory pattern (`create_app()`)
- CLI command to initialize the database (`flask init-db`)
- RESTful endpoints with JSON responses
- Ready for testing and development
