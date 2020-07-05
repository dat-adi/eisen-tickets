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
    def __init__(self, category, content, more_info):
        self.category = category
        self.timestamp = dt.now()
        self.content = content
        self.more_info = more_info
        self.ticket_info = {"Time Stamp" : self.timestamp, "Category" : self.category, "Content" : self.content, "More Info" : self.more_info}

    def change_category(self, category):
        self.category = category

    def change_content(self, content):
        self.content = content

    def add_more_info(self, more_info):
        self.more_info = more_info

    def return_ticket_info(self):
        return self.ticket_info

if __name__ == "__main__":
    sample_ticket = ticket_maker("test_category", "testing it out", "a little more to go on")
    print("Time stamp : {}\nCategory : {}\nContent : {}\nMore Info : {}".format(sample_ticket.timestamp, sample_ticket.category, sample_ticket.content, sample_ticket.more_info))
