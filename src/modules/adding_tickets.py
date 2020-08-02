import tkinter as tk
from tkinter import ttk
from modules.create_db_components import create_connection


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
        for F in (MainPage, TicketAdd):
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


class TicketAdd(tk.Frame):
    def __init__(self, parent, controller, conn):
        tk.Frame.__init__(self, parent)
        self.conn = conn
        fields = ['Category', 'Task', 'More Info']

        r = 0
        for field in fields:
            tk.Label(self, text=field, relief=tk.RIDGE, width=15).grid(row=r, column=0)
            r += 1

        cat_entry = ttk.Entry(self)
        cat_entry.grid(row=0, column=1)

        task_entry = ttk.Entry(self)
        task_entry.grid(row=1, column=1)

        more_info_entry = ttk.Entry(self)
        more_info_entry.grid(row=2, column=1)

        ticket_details = [cat_entry.get(), task_entry.get(), more_info_entry.get()]
        print(ticket_details)

        switch_window_button = tk.Button(self, text="Add a ticket", command=lambda: controller.show_frame(MainPage))
        switch_window_button.grid(row=5, column=1)


if __name__ == '__main__':
    test_window = windows(create_connection(r"D:\eisen-tickets\assets\tickets.db"))
    test_window.mainloop()
