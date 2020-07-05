from modules.ticket_header import ticket_maker

if __name__ == "__main__":

    version_info = open("../assets/version.txt", 'r').read()
    print("Eisenhower Tickets | " + version_info)
    print("Categories")
    print("-"*10)

    print("1. Do       - Urgent and Important")
    print("2. Decide   - Not Urgent and Important")
    print("3. Delegate - Urgent and Not Important")
    print("4. Delete   - Not Urgent and Not Important\n")

    categories = ["DO", "DEC", "DLG", "DEL"]
    category_number = int(input("Enter the category number : "))
    content = input("Enter the task at hand : ")
    more_info = input("Enter details of task : ")
    category = categories[category_number-1]

    print("Ticket Created\n")

    print("Ticket Details")
    print("-"*45)
    sample_ticket = ticket_maker(category, content, more_info)
    print("Time stamp : {}".format(sample_ticket.timestamp))
    print("Category   : {}".format(sample_ticket.category))
    print("-"*45)
    print("Content    : {}".format(sample_ticket.content))
    print("-"*45)
    print("More Info  : {}".format(sample_ticket.more_info))
    print("-"*45)
