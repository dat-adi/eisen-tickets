import tkinter as tk
from modules.create_db_components import create_connection


def do_cat(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM tickets WHERE category = "DO"')
    conn.commit()
    rows = cur.fetchall()

    return rows


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, TestPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        test_button = tk.Button(self, text="Visit Test Page", command=lambda: controller.show_frame(TestPage))
        test_button.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Back To Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Back To Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()


class TestPage(tk.Frame):
    def __init__(self, parent, controller):
        self.conn = create_connection(r"D:\eisen-tickets\assets\tickets.db")
        tk.Frame.__init__(self, parent)
        do_rows = do_cat(self.conn)
        for element in do_rows:
            tk.Button(self, text=element[3], fg="black").pack(fill=tk.X)

        return_button = tk.Button(self, text="Return to main page", command=lambda: controller.show_frame(StartPage))
        return_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    app = windows()
    app.mainloop()
