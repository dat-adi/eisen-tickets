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


def main():
    conn = create_connection(r"D:\eisen-tickets\assets\test2.db")
    create_sql_table = '''CREATE TABLE IF NOT EXISTS tickets (
                            id integer PRIMARY KEY,
                            timestamp text NOT NULL,
                            category text NOT NULL,
                            task text NOT NULL,
                            more_info text
                        );'''
    if conn is not None:
        create_table(conn, create_sql_table)
        ticket_1 = ("09/10/2020", "DO", "Study Math", "Math is pretty much always a to be studied.")
        ticket_2 = ("19/10/2020", "DO", "Study Math", "Math is always a to be studied.")
        insertion_row(conn, ticket_1)
        insertion_row(conn, ticket_2)

if __name__ == "__main__":
    main()