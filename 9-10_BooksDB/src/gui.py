"""Module for GUI functions."""

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from src.validation import *
from src.database import *

def submit(root, title, author, isbn, copies_purchased, copies_not_checked_out, retail_price):
    """Submit book information."""
    validate_author(author.get())
    validate_isbn(isbn.get())
    validate_copies_purchased(copies_purchased.get())
    validate_copies_not_checked_out(copies_not_checked_out.get())
    validate_retail_price(retail_price.get())

    add_book(title.get(), author.get(), isbn.get(), copies_purchased.get(), copies_not_checked_out.get(), retail_price.get())

    # Clearing Entry widgets
    title.delete(0, END)
    author.delete(0, END)
    isbn.delete(0, END)
    copies_purchased.delete(0, END)
    copies_not_checked_out.delete(0, END)
    retail_price.delete(0, END)

def show_books():
    """Display all books."""
    # Your implementation here

def delete(book_id):
    """Delete a book."""
    # Your implementation here

def edit_book(book_id):
    """Edit a book."""
    # Your implementation here

def go_back():
    """Go back to the main screen."""
    # Your implementation here

def main():
    """Main function."""
    # Your main window code here

if __name__ == "__main__":
    main()
