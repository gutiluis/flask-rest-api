import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def get_db():
    """open a sqlite connection for the current request if one doesnt exist. stores it in flask.g. rows are returned as dictionary like objects"""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# function needs to be registered with the application instance. register the application
def close_db(e=None):
    """cloes after request ends"""
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


# function needs to be registered with the application instance. register the application
# create flask cli
@click.command("init-db")
def init_db_command():
    """clear existing data and create new tables."""
    init_db()
    click.echo("initialized the database")

# ensure sqlite automatically converts timestamp strings to python datetime objects when reading from the database
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)