> [!WARNING]
> CURRENTLY UNDER DEVELOPMENT

# Flask REST API

REST API built with Flask and SQLite using the application factory pattern, database helpers, and CLI commands.

---

## How it works:

```
python3 -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### Setup database

### run init-db to make an instance folder and initialize the sqlitedb from the schema.sql file

```
flask --app flask_test_dir init-db
```

---

## Features

- SQLite database integration
- Application factory pattern (create_app())
- CLI command to initialize the database (flask init-db)

---

## Tech-Stack

- Python
- Flask

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see CONTRIBUTING.md for more information on what we're looking for and how to get started.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on the Community page.

---

## License
This project is licensed under the [MIT License](LICENSE).
