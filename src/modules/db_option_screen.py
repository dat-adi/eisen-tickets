
def option_screen():
    print("Pick one of the options below to proceed further.")
    print('-' * 10)
    print("1. Display existing tickets")
    print("2. Create new ticket")
    print('-' * 10)
    choice = input('choice> ')
    if choice is 1:
        print("Pick an option to display the field you would like : ")

        print("1. Do       - Urgent and Important")
        print("2. Decide   - Not Urgent and Important")
        print("3. Delegate - Urgent and Not Important")
        print("4. Delete   - Not Urgent and Not Important\n")
        print("5. All fields")
        return int(input())
    elif choice is 2:
        return 6

    '''
if choice is 1:
    display_info()
elif choice is 2:
    print("Starting up the selection screen...")
    table_initialization()
    print("Adding Ticket to Eisen's Tickets...")
    '''
