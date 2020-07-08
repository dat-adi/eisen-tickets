import json

def ticket_alloter(category):
    if category is "DO":
        with open("../assets/do.txt", "w") as f:
            try:
                tickets = json.load(f)
                keys_in_tickets = [int(key) for key in tickets.keys()]
                return max(keys_in_tickets) + 1
            except:
                return 1
    if category is "DEC":
        with open("../assets/dec.txt", "w") as f:
            try:
                tickets = json.load(f)
                keys_in_tickets = [int(key) for key in tickets.keys()]
                return max(keys_in_tickets) + 1
            except:
                return 1
    if category is "DLG":
        with open("../assets/dlg.txt", "w") as f:
            try:
                tickets = json.load(f)
                keys_in_tickets = [int(key) for key in tickets.keys()]
                return max(keys_in_tickets) + 1
            except:
                return 1
    if category is "DEL":
        with open("../assets/del.txt", "w") as f:
            try:
                tickets = json.load(f)
                keys_in_tickets = [int(key) for key in tickets.keys()]
                return max(keys_in_tickets) + 1
            except:
                return 1

if __name__ == "__main__":
    ticket_alloter()
