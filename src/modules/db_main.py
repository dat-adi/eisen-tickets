from modules.create_db_components import insertion_row, create_connection, create_table
from modules.db_ticket_maker import selection


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
        ticket = selection()
        insertion_row(conn, ticket)


if __name__ == "__main__":
    table_initialization()
