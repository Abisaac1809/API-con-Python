import sqlite3
from errors.server_errors import DatabaseConnectionError

DB_PATH = "db.sqlite3"

_CREATE_TABLES_STATEMENT = """
    CREATE TABLE IF NOT EXISTS users (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        name       TEXT    NOT NULL,
        email      TEXT    NOT NULL UNIQUE,
        phone      TEXT    NOT NULL UNIQUE,
        password   TEXT    NOT NULL,
        created_at TEXT    NOT NULL,
        updated_at TEXT    NOT NULL
    )
    """


def get_connection() -> sqlite3.Connection:
    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error:
        raise DatabaseConnectionError()


def init_db() -> None:
    try:
        with get_connection() as connection:
            connection.execute(_CREATE_TABLES_STATEMENT)
    except sqlite3.Error:
        raise DatabaseConnectionError()
