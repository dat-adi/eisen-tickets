#!/usr/bin/python
# -*- coding: utf-8 -*-

# Directs to the db_main where it connects to the database and displays info.
from modules.db_main import table_initialization

"""This piece of code acts as the hub for CLI users."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


if __name__ == "__main__":

    version_info = open("../assets/version.txt", "r").read()
    print("Eisenhower Tickets | " + version_info)

    while True:
        print("Starting up the selection screen...")
        table_initialization()
        cont = input("Do you wish to restart the service? (y/n) : ")
        if cont == "n":
            print("Exiting Eisen's Tickets...")
            break
        print("Restarting Eisen's Tickets...")
        print("-" * 10)
        print()
