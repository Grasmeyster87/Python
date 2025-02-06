import sqlite3

DB_NAME = "./Раздел 54 - Работа с базой данных SQLite/DB/sqlite_db.db"


def create_db(name_DB):
    with sqlite3.connect(name_DB) as sqlite_conn:
        print(sqlite_conn)
        print(sqlite3.version)

# create_db(DB_NAME)


def create_table(name_DB):
    with sqlite3.connect(name_DB) as sqlite_conn:
        sqlite_request = """CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        students_qty integer,
        reviews_qty integer
        );"""
        sqlite_conn.execute(sqlite_request)


create_table(DB_NAME)
