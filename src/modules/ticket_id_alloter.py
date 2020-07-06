import json

def ticket_alloter():
    with open("../assets/eisen-tickets.txt", 'r') as f:
        tickets = json.load(f)
        keys_in_tickets = [int(key) for key in tickets.keys()]
        return max(keys_in_tickets) + 1

if __name__ == "__main__":
    ticket_alloter()
