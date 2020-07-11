from modules.db_main import table_initialization

if __name__ == "__main__":

    version_info = open("../assets/version.txt", 'r').read()
    print("Eisenhower Tickets | " + version_info)
    print("Starting up the selection screen...")
    table_initialization()
