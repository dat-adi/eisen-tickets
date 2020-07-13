from tkinter import *


class display_ticket:
    def __init__(self, ticket):
        self.id = ticket[0]
        self.timestamp = ticket[1]
        self.category = ticket[2]
        self.task = ticket[3]
        self.more_info = ticket[4]

        self.root = Tk()

    def tkinter_display(self):
        self.root.title("Ticket Info")

        fields = ['Ticket ID', 'Timestamp', 'Category', 'Task', 'More Info']
        details = [self.id, self.timestamp, self.category, self.task, self.more_info]

        r = 0
        for field in fields:
            Label(text=field, relief=RIDGE, width=15).grid(row=r, column=0)
            Label(text=details[r], relief=SUNKEN, width=100).grid(row=r, column=1)
            r += 1

        self.root.mainloop()

def ticket_retriever(ticket):
    display_ticket(ticket).tkinter_display()


if __name__ == "__main__":
    ticket = (1, "23/34/12", "DO", "something", "random text alsdnf alskdf ;lasmdflknasldfnasndflknaskdnfkansdlkfjaknsdjf")
    ticket_retriever(ticket)
