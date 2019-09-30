import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    this function initializes a database by creating a database connection
    and connection cursor. It also Drops the sparkifydb if it exists before
    attempting to create it.

    the function returns a connection and cursor object to interact with
    the database.

    Arguments:
        None

    Returns:
        cur: the cursor object.
        conn: the connection object.
    """
    # connect to default database
    conn_str = "host=127.0.0.1 dbname=studentdb user=student password=student"
    conn = psycopg2.connect(conn_str)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute(
        "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn_str = "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drop all the tables

    the function returns a connection and cursor object to interact
    with the database.

    Arguments:
        cur: database cursor
        conn: database connection

    Returns:
        None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create all the tables

    the function returns a connection and cursor object to
    interact with the database.

    Arguments:
        cur: database cursor
        conn: database connection

    Returns:
        None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Used to reset the database

    Drops all the tabled and then creates them.

    Arguments:
        None

    Returns:
        None
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
