from tkinter import *
from modules.create_db_components import create_connection

def do_cat(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE category = DO")
    conn.commit()
    rows = cur.fetchall()

    return rows

def dec_cat(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE category = DEC")
    conn.commit()
    rows = cur.fetchall()

    return rows

def dlg_cat(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE category = DLG")
    conn.commit()
    rows = cur.fetchall()

    return rows

def del_cat(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE category = DEL")
    conn.commit()
    rows = cur.fetchall()

    return rows

def labels_in_screen(conn, ltf, rtf, lbf, rbf):

    do_rows = do_cat(conn)
    for element in do_rows:
        Label(ltf, text=element)
    dec_rows = dec_cat(conn)
    for element in dec_rows:
        Label(rtf, text=element)
    dlg_rows = dlg_cat(conn)
    for element in dlg_rows:
        Label(lbf, text=element)
    del_rows = del_cat(conn)
    for element in del_rows:
        Label(rbf, text=element)


def screens(conn):
    root = Tk()

    mainFrame = Frame(root, height= 400, width=600)
    mainFrame.pack()

    topRow = Frame(mainFrame, height=200, width=600)
    topRow.pack(side=TOP)

    bottomRow  = Frame(mainFrame, height=200, width=600)
    bottomRow.pack(side=BOTTOM)

    leftTopFrame = Frame(topRow, height=200, width=300, bg="red")
    leftTopFrame.pack(side=LEFT)

    rightTopFrame = Frame(topRow, height=200, width=300)
    rightTopFrame.pack(side=RIGHT)

    leftBottomFrame = Frame(bottomRow, height=200, width=300)
    leftBottomFrame.pack(side=LEFT)

    rightBottomFrame = Frame(bottomRow, height=200, width=300)
    rightBottomFrame.pack(side=RIGHT)

    labels_in_screen(conn, leftTopFrame, rightTopFrame, leftBottomFrame, rightBottomFrame)

    root.mainloop()

if __name__ == "__main__":
    connection = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    screens(connection)


