#!/usr/bin/python
# -*- coding: utf-8 -*-

# importing for operations on the database
import sqlite3
from sqlite3 import Error

'''This module contains functions to connect, create and insert into the database.'''

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


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

