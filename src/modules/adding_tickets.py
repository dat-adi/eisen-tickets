#!/usr/bin/python
# -*- coding: utf-8 -*-

# GUI import
import tkinter as tk

# Styling the GUI
from tkinter import ttk

# Connecting, creating, and inserting into a database
from modules.create_db_components import insertion_row, create_connection, create_table

# Creating a ticket
from modules.db_ticket_maker import ticket_maker

# GUI addition
from modules.location_designator import location_gui_retrieval


'''This module is used to add new tickets into the database.'''

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


class windows(tk.Tk):
    def __init__(self, conn, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Eisen's Tickets")
        self.iconbitmap(self, default="../../assets/logo.ico")
        self.conn = conn

        create_sql_table = '''CREATE TABLE IF NOT EXISTS tickets (
                                id integer PRIMARY KEY,
                                timestamp text NOT NULL,
                                category text NOT NULL,
                                task text NOT NULL,
                                more_info text
                            );'''

        if conn is not None:
            create_table(conn, create_sql_table)

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, TicketAdd, CompletionScreen):
            frame = F(container, self, self.conn)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        self.conn = conn
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(self, text="Add a ticket", command=lambda: controller.show_frame(TicketAdd))
        switch_window_button.pack(side="bottom", fill=tk.X)


def ticket_insertion(conn, cat_entry, task_entry, more_info_entry):
    ticket = ticket_maker(cat_entry, task_entry.get(), more_info_entry.get()).return_ticket_info()
    insertion_row(conn, ticket)


def radio_selection(v):
    categories = ['DO', 'DEC', 'DLG', 'DEL']
    v.get()
    cate = categories[v.get()]
    return cate


class TicketAdd(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        self.conn = conn
        fields = ['Category', 'Task', 'More Info']
        v = tk.IntVar()

        r = 0
        for field in fields:
            tk.Label(self, text=field, relief=tk.RIDGE, width=15).grid(row=r, column=0)
            r += 1

        cat_entry_do = tk.Radiobutton(self, text="DO", padx=20, variable=v, value=0)
        cat_entry_do.grid(row=0, column=1)
        cat_entry_dec = tk.Radiobutton(self, text="DEC", padx=20, variable=v, value=1)
        cat_entry_dec.grid(row=0, column=2)
        cat_entry_dlg = tk.Radiobutton(self, text="DLG", padx=20, variable=v, value=2)
        cat_entry_dlg.grid(row=0, column=3)
        cat_entry_del = tk.Radiobutton(self, text="DEL", padx=20, variable=v, value=3)
        cat_entry_del.grid(row=0, column=4)

        task_entry = ttk.Entry(self)
        task_entry.grid(row=1, column=1, columnspan=5, sticky=tk.W+tk.E)

        more_info_entry = ttk.Entry(self)
        more_info_entry.grid(row=2, column=1, columnspan=5, sticky=tk.W+tk.E)

        switch_window_button = tk.Button(self, text="Cancel", command=lambda: controller.show_frame(MainPage))
        switch_window_button.grid(row=5, column=0)
        submit_button = tk.Button(self, text="Submit",
                                  command=lambda: [ticket_insertion(self.conn, radio_selection(v), task_entry,
                                                                    more_info_entry),
                                                   controller.show_frame(CompletionScreen)])
        submit_button.grid(row=5, column=1)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        self.conn = conn
        tk.Label(self, text="Ticket Added Successfully.").pack(padx=10, pady=10)
        switch_window_button = ttk.Button(self, text="Return to menu", command=lambda: controller.show_frame(MainPage))
        switch_window_button.pack(side="bottom", fill=tk.X)


if __name__ == '__main__':
    db_conn = location_gui_retrieval()
    test_window = windows(create_connection(db_conn))
    test_window.mainloop()
