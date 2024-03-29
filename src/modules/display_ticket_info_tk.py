#!/usr/bin/python
# -*- coding: utf-8 -*-

# Loading in GUI components for the ticket info to be displayed.
from tkinter import Label, RIDGE, SUNKEN, Tk

"""This module is used to display the tickets in a tkinter grid format."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


class display_ticket:
    def __init__(self, ticket):
        self.id = ticket[0]
        self.timestamp = ticket[1]
        self.category = ticket[2]
        self.task = ticket[3]
        self.more_info = ticket[4]
        self.fields = ["Ticket ID", "Timestamp", "Category", "Task", "More Info"]
        self.details = [
            self.id,
            self.timestamp,
            self.category,
            self.task,
            self.more_info,
        ]

        self.root = Tk()

    def tkinter_display(self):
        self.root.title("Ticket Info")

        r = 0
        for field in self.fields:
            Label(text=field, relief=RIDGE, width=15).grid(row=r, column=0)
            Label(text=self.details[r], relief=SUNKEN, width=100).grid(row=r, column=1)
            r += 1

        self.root.mainloop()


def ticket_retriever(ticket):
    display_ticket(ticket).tkinter_display()


if __name__ == "__main__":
    tick = (1, "23/34/12", "DO", "something", "random text lul")
    ticket_retriever(tick)
