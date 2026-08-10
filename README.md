> [!WARNING]
> CURRENTLY UNDER DEVELOPMENT

# Flask REST API

REST API built with Flask and SQLite using the application factory pattern, database helpers, and CLI commands.

---

## How it works

```
git clone https://github.com/gutiluis/flask-rest-api.git
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
- sqlite3

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see [CONTRIBUTING.md](https://github.com/gutiluis/.github/blob/main/CONTRIBUTING.md) for more information on what we're looking for and how to get started.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](https://github.com/gutiluis/.github/blob/main/CODE_OF_CONDUCT.md).

---

## Security Policy

If you discover a security vulnerability, please review our [Security Policy](https://github.com/gutiluis/.github/blob/main/SECURITY.md) for reporting guidelines.

---

## Support

If you run into any issues or have questions, please check our [SUPPORT.md](https://github.com/gutiluis/.github/blob/main/SUPPORT.md) file for guidance, or reach out through one of our community channels below.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on our **Community** channels:
* **Discord:** [Community channel](https://discord.gg/5xdAFuadP)
* **Slack Workspace:** [technobool.slack.com](https://technobool.slack.com)
* **GitHub Discussions:** [Open a discussion](https://github.com/gutiluis/flask-rest-api/discussions)

---

## License

[MIT LICENSE](LICENSE)
