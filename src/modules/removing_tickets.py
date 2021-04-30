#!/usr/bin/python
# -*- coding: utf-8 -*-

# Database connection
from modules.create_db_components import create_connection

"""This module is used to contain the function that can remove the ticket from the database."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


# this function connects and removes the requested ticket
def delete_ticket(connect, ticket_id):
    delete_query = """DELETE FROM tickets
                      WHERE id=?"""
    cur = connect.cursor()
    cur.execute(delete_query, (ticket_id,))
    connect.commit()
    print(str(ticket_id) + " has been deleted now.")


if __name__ == "__main__":
    conn = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    delete_ticket(conn, 1)
