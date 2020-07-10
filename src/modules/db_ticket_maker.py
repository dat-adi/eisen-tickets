from datetime import datetime as dt


class ticket_maker:
    def __init__(self, category, task, more_info):
        self.category = category
        self.timestamp = dt.now()
        self.task = task
        self.more_info = more_info

        self.ticket = (self.timestamp, self.category, self.task, self.more_info)

    def change_category(self, category):
        self.category = category

    def change_task(self, task):
        self.task = task

    def add_more_info(self, more_info):
        self.more_info = more_info

    def return_ticket_info(self):
        return self.ticket

    def return_category(self):
        return self.category


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
    print("[INFO] Ticket Created...\n")
    return ticket_maker(category, task, more_info).return_ticket_info()
