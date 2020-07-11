from modules.create_db_components import insertion_row, create_connection, create_table
from modules.db_ticket_maker import selection
from modules.db_option_screen import option_screen
from modules.db_display import display_info_category, display_info


def table_initialization():
    conn = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    create_sql_table = '''CREATE TABLE IF NOT EXISTS tickets (
                            id integer PRIMARY KEY,
                            timestamp text NOT NULL,
                            category text NOT NULL,
                            task text NOT NULL,
                            more_info text
                        );'''
    if conn is not None:
        create_table(conn, create_sql_table)
        response = option_screen()
        if response == 1:
            display_info_category(conn, "DO")
        elif response == 2:
            display_info_category(conn, "DEC")
        elif response == 3:
            display_info_category(conn, "DLG")
        elif response == 4:
            display_info_category(conn, "DEL")
        elif response == 5:
            display_info(conn)
        elif response == 6:
            while True:
                ticket = selection()
                insertion_row(conn, ticket)
                print("Adding Ticket to Eisen's Tickets...")
                if input("Do you wish to continue adding entries? (y/n) : ") == 'n':
                    break


if __name__ == "__main__":
    table_initialization()
