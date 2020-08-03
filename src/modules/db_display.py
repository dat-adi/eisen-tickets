#!/usr/bin/python
# -*- coding: utf-8 -*-

# Connecting to the database
from modules.create_db_components import create_connection


'''This module is used to display ticket information from the database.'''

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


def display_info(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets")
    conn.commit()
    rows = cur.fetchall()

    for element in rows:
        print(element)


def display_info_category(conn, category):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE category = ?", (category,))
    conn.commit()
    rows = cur.fetchall()

    for element in rows:
        print(element)


if __name__ == "__main__":
    connection = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    display_info_category(connection, "DO")
