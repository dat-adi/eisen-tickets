from modules.db_insertion import create_table, insertion_row, create_connection


def main():
    database = r"D:\eisen-tickets\assets\test.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        category text,
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    timestamp text NOT NULL,
                                    category text NOT NULL,
                                    task text NOT NULL,
                                    project_id integer NOT NULL,
                                    more_info text,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)

        project_id = create_table(conn, sql_create_tasks_table)
        details = ('09/01/2020', "DO", "nothing", project_id, "doing absolutely nothing might lead to a higher level of understanding.")
        insertion_row(conn, details)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()