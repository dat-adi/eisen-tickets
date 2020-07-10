import sqlite3
from sqlite3 import Error


def insertion_row(conn, ticket):
    sql = """INSERT INTO tickets (timestamp, category, task, more_info) \
                  VALUES (?, ?, ?, ?);"""
    cur = conn.cursor()
    cur.execute(sql, ticket)
    conn.commit()
    return cur.lastrowid


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

