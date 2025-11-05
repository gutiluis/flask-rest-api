# Flask REST API
# RESTful API built with Flask and SQLite using the application factory pattern, database helpers, and CLI commands.

# How to create a virtual environment:
- python3 -m venv venv
- source venv/bin/activate # macOS/Linux
- venv\Scripts\activate    # Windows

# Install dependencies
- pip install -r requirements.txt

# Setup database
# run the init-db command to make an instance folder and initialize the sqlitedb from the schema.sql file
- flask --app flask_test_dir init-db


## Features
- SQLite database integration
- Application factory pattern (`create_app()`)
- CLI command to initialize the database (`flask init-db`)


## License
This project is licensed under the [MIT License](LICENSE).
