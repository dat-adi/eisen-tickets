import json

def category_write(ticket, category):
    if category is "DO":
        with open("../assets/do.txt", "w") as f:
            f.write(json.dumps(ticket))
    if category is "DEC":
        with open("../assets/dec.txt", "w") as f:
            f.write(json.dumps(ticket))
    if category is "DLG":
        with open("../assets/dlg.txt", "w") as f:
            f.write(json.dumps(ticket))
    if category is "DEL":
        with open("../assets/del.txt", "w") as f:
            f.write(json.dumps(ticket))
