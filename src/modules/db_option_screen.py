
def option_screen():
    print("Pick one of the options below to proceed further.")
    print('-' * 10)
    print("1. Display existing tickets")
    print("2. Create new ticket")
    print('-' * 10)
    choice = int(input('choice> '))
    if choice == 1:
        print("Pick an option to display the field you would like : ")

        print("1. Do       - Urgent and Important")
        print("2. Decide   - Not Urgent and Important")
        print("3. Delegate - Urgent and Not Important")
        print("4. Delete   - Not Urgent and Not Important")
        print("5. All fields\n")
        return int(input("Enter option : "))
    elif choice == 2:
        return 6
