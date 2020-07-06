import json
from modules.ticket_header import selection

if __name__ == "__main__":

    version_info = open("../assets/version.txt", 'r').read()
    print("Eisenhower Tickets | " + version_info)
    ticket = selection()
    print("Adding Ticket to Eisen's Tickets...")
    
    with open("../assets/eisen-tickets.txt", 'w') as f:
        f.write(json.dumps(ticket))

