import tkinter as tk
from modules.display_ticket_info_tk import ticket_retriever
from modules.create_db_components import create_connection


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


class windows(tk.Tk):
    def __init__(self, conn, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.conn = conn

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, DoPage, DecPage, DlgPage, DelPage):
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
        label = tk.Label(self, text="Start Page")
        label.pack(padx=10, pady=10)

        do_button = tk.Button(self, text="Eisen Do", command=lambda: controller.show_frame(DoPage))
        do_button.pack(fill=tk.X)
        dec_button = tk.Button(self, text="Eisen Decide", command=lambda: controller.show_frame(DecPage))
        dec_button.pack(fill=tk.X)
        dlg_button = tk.Button(self, text="Eisen Delegate", command=lambda: controller.show_frame(DlgPage))
        dlg_button.pack(fill=tk.X)
        del_button = tk.Button(self, text="Eisen Delete", command=lambda: controller.show_frame(DelPage))
        del_button.pack(fill=tk.X)


class DoPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Do Page")
        label.pack(padx=10, pady=10)

        do_rows = do_cat(conn)
        for element in do_rows:
            tk.Button(self, text=element[3], fg="black").pack(fill=tk.X)

        dec_button = tk.Button(self, text="Eisen Decide", command=lambda: controller.show_frame(DecPage))
        dec_button.pack(fill=tk.X)
        dlg_button = tk.Button(self, text="Eisen Delegate", command=lambda: controller.show_frame(DlgPage))
        dlg_button.pack(fill=tk.X)
        del_button = tk.Button(self, text="Eisen Delete", command=lambda: controller.show_frame(DelPage))
        del_button.pack(fill=tk.X)
        main_button = tk.Button(self, text="Return to main page", command=lambda: controller.show_frame(MainPage))
        main_button.pack(side="bottom", fill=tk.X)


class DecPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Decide Page")
        label.pack(padx=10, pady=10)

        dec_rows = dec_cat(conn)
        for element in dec_rows:
            tk.Button(self, text=element[3], fg="black").pack(fill=tk.X)

        do_button = tk.Button(self, text="Eisen Do", command=lambda: controller.show_frame(DoPage))
        do_button.pack(fill=tk.X)
        dlg_button = tk.Button(self, text="Eisen Delegate", command=lambda: controller.show_frame(DlgPage))
        dlg_button.pack(fill=tk.X)
        del_button = tk.Button(self, text="Eisen Delete", command=lambda: controller.show_frame(DelPage))
        del_button.pack(fill=tk.X)
        main_button = tk.Button(self, text="Return to main page", command=lambda: controller.show_frame(MainPage))
        main_button.pack(side="bottom", fill=tk.X)


class DlgPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Delegate Page")
        label.pack(padx=10, pady=10)

        dlg_rows = dlg_cat(conn)
        for element in dlg_rows:
            tk.Button(self, text=element[3], fg="black").pack(fill=tk.X)

        do_button = tk.Button(self, text="Eisen Do", command=lambda: controller.show_frame(DoPage))
        do_button.pack(fill=tk.X)
        dec_button = tk.Button(self, text="Eisen Decide", command=lambda: controller.show_frame(DecPage))
        dec_button.pack(fill=tk.X)
        del_button = tk.Button(self, text="Eisen Delete", command=lambda: controller.show_frame(DelPage))
        del_button.pack(fill=tk.X)
        main_button = tk.Button(self, text="Return to main page", command=lambda: controller.show_frame(MainPage))
        main_button.pack(side="bottom", fill=tk.X)


class DelPage(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Eisen's Delete Page")
        label.pack(padx=10, pady=10)

        del_rows = del_cat(conn)
        for element in del_rows:
            tk.Button(self, text=element[3], fg="black").pack(fill=tk.X)

        do_button = tk.Button(self, text="Eisen Do", command=lambda: controller.show_frame(DoPage))
        do_button.pack(fill=tk.X)
        dec_button = tk.Button(self, text="Eisen Decide", command=lambda: controller.show_frame(DecPage))
        dec_button.pack(fill=tk.X)
        dlg_button = tk.Button(self, text="Eisen Delegate", command=lambda: controller.show_frame(DlgPage))
        dlg_button.pack(fill=tk.X)
        main_button = tk.Button(self, text="Return to main page", command=lambda: controller.show_frame(MainPage))
        main_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    connection = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    four_windows = windows(connection)
    four_windows.mainloop()
