from modules.create_db_components import create_connection


def delete_ticket(connect, ticket_id):
    delete_query = '''DELETE FROM tickets
                      WHERE id=?'''
    cur = connect.cursor()
    cur.execute(delete_query, (ticket_id, ))
    connect.commit()
    print(str(ticket_id) + " has been deleted now.")


if __name__ == '__main__':
    conn = create_connection(r"D:\eisen-tickets\assets\tickets.db")
    delete_ticket(conn, 1)
