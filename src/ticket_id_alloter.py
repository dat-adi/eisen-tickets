import json

def ticket_alloter():
    with open("../assets/eisen-tickets.txt", 'r') as f:
        tickets = json.load(f)
        for key, value in tickets.items():
            print("Key", key)
            print("Value", value)

if __name__ == "__main__":
    ticket_alloter()
