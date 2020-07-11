from modules.db_main import table_initialization

if __name__ == "__main__":

    version_info = open("../assets/version.txt", 'r').read()
    print("Eisenhower Tickets | " + version_info)

    while True:
        print("Starting up the selection screen...")
        table_initialization()
        cont = input("Do you wish to restart the service? (y/n) : ")
        if cont is 'n':
            print("Exiting Eisen's Tickets...")
            break
        print("Restarting Eisen's Tickets...")
        print('-'*10)
        print()
