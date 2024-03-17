"""Module for database operations."""

import sqlite3

def add_book(title, author, isbn, copies_purchased, copies_not_checked_out, retail_price):
    """Add a book to the database."""
    conn = sqlite3.connect('Books.db')
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?, ?)",
              (
                  title,
                  author,
                  isbn,
                  copies_purchased,
                  copies_not_checked_out,
                  retail_price
              )
              )
    conn.commit()
    conn.close()

def delete_book(book_id):
    """Delete a book from the database."""
    conn = sqlite3.connect('Books.db')
    c = conn.cursor()
    c.execute("DELETE from books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()

def get_all_books():
    """Retrieve all books from the database."""
    conn = sqlite3.connect('Books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return books
