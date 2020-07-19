from tkinter import *
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


class windows:
    def __init__(self, conn):
        self.root = Tk()
        self.conn = conn

        self.mainFrame = Frame(self.root, height=400, width=600)
        self.mainFrame.pack()

        self.topRow = Frame(self.mainFrame, height=200, width=600)
        self.topRow.pack(side=TOP)

        self.bottomRow = Frame(self.mainFrame, height=200, width=600)
        self.bottomRow.pack(side=BOTTOM)

        self.leftTopFrame = Frame(self.topRow, height=200, width=300, bg="red")
        self.leftTopFrame.pack(side=LEFT)

        self.rightTopFrame = Frame(self.topRow, height=200, width=300)
        self.rightTopFrame.pack(side=RIGHT)

        self.leftBottomFrame = Frame(self.bottomRow, height=200, width=300)
        self.leftBottomFrame.pack(side=LEFT)

        self.rightBottomFrame = Frame(self.bottomRow, height=200, width=300)
        self.rightBottomFrame.pack(side=RIGHT)

        self.root.mainloop()

    def labels_in_screen(self):

        do_rows = do_cat(self.conn)
        for element in do_rows:
            Label(self.leftTopFrame, text=element, fg="black")
        dec_rows = dec_cat(self.conn)
        for element in dec_rows:
            Label(self.rightTopFrame, text=element, fg="black")
        dlg_rows = dlg_cat(self.conn)
        for element in dlg_rows:
            Label(self.leftBottomFrame, text=element, fg="black")
        del_rows = del_cat(self.conn)
        for element in del_rows:
            Label(self.rightBottomFrame, text=element, fg="black")

    def screens(self):

        self.labels_in_screen()


if __name__ == "__main__":
    connection = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    four_windows = windows(connection)
