#!/usr/bin/python
# -*- coding: utf-8 -*-

# GUI import
import tkinter as tk

# Styling the GUI
from tkinter import ttk

# Database connection
from modules.create_db_components import create_connection

# Deletes the ticket from the database
from modules.removing_tickets import delete_ticket

"""This module is used to display all the tickets present in the 
    Database."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"

# fonts for the project
text_font = ("Helvetica", 12)


# functions to retrieve all of the records from the database
def do_cat(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tickets WHERE category = "DO"')
    conn.commit()
    rows = cur.fetchall()

    return rows


def dec_cat(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tickets WHERE category = "DEC"')
    conn.commit()
    rows = cur.fetchall()

    return rows


def dlg_cat(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tickets WHERE category = "DLG"')
    conn.commit()
    rows = cur.fetchall()

    return rows


def del_cat(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tickets WHERE category = "DEL"')
    conn.commit()
    rows = cur.fetchall()

    return rows


# GUI for the project
class windows(tk.Tk):
    def __init__(self, conn, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Eisen's Tickets")
        self.iconbitmap(self, default="../../assets/logo.ico")
        self.conn = conn

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, EisenDisplay, DoPage, DecPage, DlgPage, DelPage):
            frame = F(container, self, self.conn)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def ticket_display(self, ticket):
        new_window = tk.Toplevel(self)
        ticket_id = ticket[0]
        timestamp = ticket[1]
        category = ticket[2]
        task = ticket[3]
        more_info = ticket[4]
        fields = ["Ticket ID", "Timestamp", "Category", "Task", "More Info"]
        details = [ticket_id, timestamp, category, task, more_info]

        r = 0
        for field in fields:
            tk.Label(new_window, text=field, relief=tk.RIDGE, width=15).grid(
                row=r, column=0
            )
            tk.Label(new_window, text=details[r], relief=tk.SUNKEN, width=100).grid(
                row=r, column=1
            )
            r += 1
        tk.Button(
            new_window,
            relief=tk.RIDGE,
            text="Delete Ticket",
            background="#FF3333",
            command=lambda: delete_ticket(self.conn, ticket_id),
        ).grid(row=r, column=0, columnspan=2, sticky="ew")


# Pages made for navigation through the different categories
class MainPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        self.conn = conn
        label = tk.Label(self, text="Start Page", font=text_font)
        label.pack(padx=10, pady=10)

        eisen_display_button = ttk.Button(
            self,
            text="Display Selection",
            command=lambda: controller.show_frame(EisenDisplay),
        )
        eisen_display_button.pack(side="bottom", fill=tk.X)


class EisenDisplay(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        self.conn = conn
        label = tk.Label(self, text="Eisen Display", font=text_font)
        label.pack(padx=10, pady=10)

        main_button = ttk.Button(
            self,
            text="Return to main page",
            command=lambda: controller.show_frame(MainPage),
        )
        main_button.pack(side="bottom", fill=tk.X)
        del_button = ttk.Button(
            self, text="Eisen Delete", command=lambda: controller.show_frame(DelPage)
        )
        del_button.pack(side="bottom", fill=tk.X)
        dlg_button = ttk.Button(
            self, text="Eisen Delegate", command=lambda: controller.show_frame(DlgPage)
        )
        dlg_button.pack(side="bottom", fill=tk.X)
        dec_button = ttk.Button(
            self, text="Eisen Decide", command=lambda: controller.show_frame(DecPage)
        )
        dec_button.pack(side="bottom", fill=tk.X)
        do_button = ttk.Button(
            self, text="Eisen Do", command=lambda: controller.show_frame(DoPage)
        )
        do_button.pack(side="bottom", fill=tk.X)


class DoPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Do Page", font=text_font)
        label.pack(padx=10, pady=10)

        do_rows = do_cat(conn)
        for element in do_rows:
            tk.Button(
                self,
                text=element[3],
                fg="black",
                command=lambda ele=element: controller.ticket_display(ele),
            ).pack(fill=tk.X)

        eisen_display_button = ttk.Button(
            self,
            text="Display Selection",
            command=lambda: controller.show_frame(EisenDisplay),
        )
        eisen_display_button.pack(side="bottom", fill=tk.X)
        dec_button = ttk.Button(
            self, text="Eisen Decide", command=lambda: controller.show_frame(DecPage)
        )
        dec_button.pack(side="bottom", fill=tk.X)


class DecPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Decide Page", font=text_font)
        label.pack(padx=10, pady=10)

        dec_rows = dec_cat(conn)
        for element in dec_rows:
            tk.Button(
                self,
                text=element[3],
                fg="black",
                command=lambda ele=element: controller.ticket_display(ele),
            ).pack(fill=tk.X)

        eisen_display_button = ttk.Button(
            self,
            text="Display Selection",
            command=lambda: controller.show_frame(EisenDisplay),
        )
        eisen_display_button.pack(side="bottom", fill=tk.X)
        dlg_button = ttk.Button(
            self, text="Eisen Delegate", command=lambda: controller.show_frame(DlgPage)
        )
        dlg_button.pack(side="bottom", fill=tk.X)


class DlgPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Delegate Page", font=text_font)
        label.pack(padx=10, pady=10)

        dlg_rows = dlg_cat(conn)
        for element in dlg_rows:
            tk.Button(
                self,
                text=element[3],
                fg="black",
                command=lambda ele=element: controller.ticket_display(ele),
            ).pack(fill=tk.X)

        eisen_display_button = ttk.Button(
            self,
            text="Display Selection",
            command=lambda: controller.show_frame(EisenDisplay),
        )
        eisen_display_button.pack(side="bottom", fill=tk.X)
        del_button = ttk.Button(
            self, text="Eisen Delete", command=lambda: controller.show_frame(DelPage)
        )
        del_button.pack(side="bottom", fill=tk.X)


class DelPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Delete Page", font=text_font)
        label.pack(padx=10, pady=10)

        del_rows = del_cat(conn)
        for element in del_rows:
            tk.Button(
                self,
                text=element[3],
                fg="black",
                command=lambda ele=element: controller.ticket_display(ele),
            ).pack(fill=tk.X)

        eisen_display_button = ttk.Button(
            self,
            text="Display Selection",
            command=lambda: controller.show_frame(EisenDisplay),
        )
        eisen_display_button.pack(side="bottom", fill=tk.X)
        do_button = ttk.Button(
            self, text="Eisen Do", command=lambda: controller.show_frame(DoPage)
        )
        do_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    connection = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    four_windows = windows(connection)
    four_windows.mainloop()
