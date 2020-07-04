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
    def __init__(self, category, content):
        self.category = category
        self.timestamp = dt.now()
        self.content = content

    def change_category(self, category):
        self.category = category

    def change_content(self, content):
        self.content = content

if __name__ == "__main__":
    sample_ticket = ticket_maker("test_category", "testing it out")
    print("Time stamp : {}\nCategory : {}\nContent : {}".format(sample_ticket.timestamp, sample_ticket.category, sample_ticket.content))
