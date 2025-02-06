import sqlite3

DB_NAME = "./Раздел 54 - Работа с базой данных SQLite/DB/sqlite_db.db"


def create_db(name_DB):
    with sqlite3.connect(name_DB) as sqlite_conn:
        print(sqlite_conn)
        print(sqlite3.version)


def create_new_table(name_DB):
    with sqlite3.connect(name_DB) as sqlite_conn:
        sqlite_request = """CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        students_qty integer,
        reviews_qty integer
        );"""
        sqlite_conn.execute(sqlite_request)


def create_new_string(name_DB):
    with sqlite3.connect(name_DB) as sqlite_conn:
        sqlite_request = """INSERT INTO courses VALUES(?, ?, ?, ?);"""
        sqlite_conn.execute(sqlite_request, (251, "Python course", 100, 30))
        sqlite_conn.commit()


def create_new_strings(name_DB, courses):
    with sqlite3.connect(name_DB) as sqlite_conn:
        sqlite_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
        for course in courses:
            sqlite_conn.execute(sqlite_request, course)
        sqlite_conn.commit()


courses = [
    (351, "JavaScript course", 415, 100),
    (614, "C++ course", 161, 10),
    (721, "Java full course", 100, 35)
]
# create_db(DB_NAME)
#  create_table(DB_NAME)
# create_new_string(DB_NAME)
create_new_strings(DB_NAME, courses)
