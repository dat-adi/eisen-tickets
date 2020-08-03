#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This module is used to display options for the CLI user."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


# This part kinda seems like it could be improved, check into it later.
def option_screen():
    print("Pick one of the options below to proceed further.")
    print('-' * 10)
    print("1. Display existing tickets")
    print("2. Create new ticket")
    print("3. Remove a ticket")
    print('-' * 10)
    choice = int(input('choice> '))
    if choice == 1:
        print("Pick an option to display the field you would like : ")

        print("1. Do       - Urgent and Important")
        print("2. Decide   - Not Urgent and Important")
        print("3. Delegate - Urgent and Not Important")
        print("4. Delete   - Not Urgent and Not Important")
        print("5. All fields\n")
        return int(input("Enter option : "))
    elif choice == 2:
        return 6
    elif choice == 3:
        return 7


if __name__ == '__main__':
    option_screen()
