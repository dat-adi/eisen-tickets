import json
from modules.ticket_header import selection
from modules.ticket_writer import category_write

if __name__ == "__main__":

    version_info = open("../assets/version.txt", 'r').read()
    print("Eisenhower Tickets | " + version_info)
    ticket, category = selection()
    print("Adding Ticket to Eisen's Tickets...")
    category_write(ticket, category)

