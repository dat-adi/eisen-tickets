# ticket header

from datetime import datetime as dt
'''
Header
------

Time stamp :
Category :

Content
-------

Task : 
'''

class ticket_maker:
    def __init__(self, ticket_id, category, task, more_info):
        self.ticket_id = ticket_id
        self.category = category
        self.timestamp = dt.now()
        self.task = task
        self.more_info = more_info

        self.ticket = {self.ticket_id : {"Time Stamp" : str(self.timestamp), "Category" : self.category, "Content" : self.task, "More Info" : self.more_info}}

    def change_category(self, category):
        self.category = category

    def change_task(self, task):
        self.task = task

    def add_more_info(self, more_info):
        self.more_info = more_info

    def return_ticket_info(self):
        return self.ticket

def selection():
    print("Categories")
    print("-"*10)

    print("1. Do       - Urgent and Important")
    print("2. Decide   - Not Urgent and Important")
    print("3. Delegate - Urgent and Not Important")
    print("4. Delete   - Not Urgent and Not Important\n")

    categories = ["DO", "DEC", "DLG", "DEL"]
    category_number = int(input("Enter the category number : "))
    task = input("Enter the task at hand : ")
    more_info = input("Enter details of task : ")
    category = categories[category_number-1]
    ticket_id = 2 # still have to work on the sorting of the ticket ids
    print("[INFO] Ticket Created...\n")

    return ticket_maker(ticket_id, category, task, more_info).return_ticket_info()
    

if __name__ == "__main__":
    sample_ticket = ticket_maker(23, "test_category", "testing it out", "a little more to go on")
    print("Ticket ID : {}\nTime stamp : {}\nCategory : {}\nTask : {}\nMore Info : {}".format(sample_ticket.ticket_id,sample_ticket.timestamp, sample_ticket.category, sample_ticket.task, sample_ticket.more_info))
    print(sample_ticket)
