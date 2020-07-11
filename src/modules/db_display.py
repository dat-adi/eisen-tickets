from modules.create_db_components import create_connection


def display_info(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets")
    conn.commit()
    rows = cur.fetchall()

    for element in rows:
        print(element)


def display_info_category(conn, category):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE category = ?", (category,))
    conn.commit()
    rows = cur.fetchall()

    for element in rows:
        print(element)


if __name__ == "__main__":
    connection = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    display_info(connection, "DO")
