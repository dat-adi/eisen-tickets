#!/usr/bin/python
# -*- coding: utf-8 -*-

# Inserting into, connecting, and creating a database
from modules.create_db_components import insertion_row, create_connection, create_table

# Selection screen for creating the type of ticket you wish to
from modules.db_ticket_maker import selection

# Simple print to explain the options provided
from modules.db_option_screen import option_screen

# Displaying information for each category
from modules.db_display import display_info_category, display_info

# Removing a ticket from the database
from modules.removing_tickets import delete_ticket

# Finding out the location of the database from db_location.txt
from modules.location_designator import location_retrieval

'''This module is used as an interface for the CLI users.'''

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


def addition_ticket(conn):
    while True:
        ticket = selection()
        insertion_row(conn, ticket)
        print("Adding Ticket to Eisen's Tickets...")
        if input("Do you wish to continue adding entries? (y/n) : ") == 'n':
            break


def remove_ticket(conn):
    while True:
        display_info(conn)
        ticket_id = int(input("Enter the ticket id of the ticket you wish to delete : "))
        delete_ticket(conn, ticket_id)
        print("Removing the ticket from Eisen's Tickets...")
        if input("Do you wish to continue removing tickets? (y/n) : ") == 'n':
            break


def table_initialization():
    db_loc = location_retrieval()
    conn = create_connection(db_loc)
    create_sql_table = '''CREATE TABLE IF NOT EXISTS tickets (
                            id integer PRIMARY KEY,
                            timestamp text NOT NULL,
                            category text NOT NULL,
                            task text NOT NULL,
                            more_info text
                        );'''
    if conn is not None:
        create_table(conn, create_sql_table)
        response = option_screen()
        if response == 1:
            display_info_category(conn, "DO")
        elif response == 2:
            display_info_category(conn, "DEC")
        elif response == 3:
            display_info_category(conn, "DLG")
        elif response == 4:
            display_info_category(conn, "DEL")
        elif response == 5:
            display_info(conn)
        elif response == 6:
            addition_ticket(conn)
        elif response == 7:
            remove_ticket(conn)


if __name__ == "__main__":
    table_initialization()
