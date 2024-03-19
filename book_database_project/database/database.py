# database.py

import sqlite3

class Database:
    """Class to handle database operations."""

    def __init__(self, db_name='Books.db'):
        """Initialize Database instance."""
        self.db_name = db_name
        self.create_books_table()  # Call method to create the books table

    def connect(self):
        """Connect to the SQLite database."""
        return sqlite3.connect(self.db_name)

    def close(self, conn):
        """Close the database connection."""
        conn.close()

    def create_books_table(self):
        """Create the books table if it does not exist."""
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn TEXT
        )
        """
        self.execute_query(query)

    def execute_query(self, query, parameters=None):
        """
        Execute SQL query on the database.

        Args:
            query (str): SQL query string.
            parameters (tuple): Parameters to be substituted into the query.

        Returns:
            cursor: Cursor object for fetching results.
        """
        conn = self.connect()
        cursor = conn.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor

    def fetch_all(self, query, parameters=None):
        """
        Fetch all records from the database.

        Args:
            query (str): SQL query string.
            parameters (tuple): Parameters to be substituted into the query.

        Returns:
            list: List of tuples containing fetched records.
        """
        cursor = self.execute_query(query, parameters)
        records = cursor.fetchall()
        self.close(cursor.connection)
        return records