from tkinter import Toplevel, Label, Button, Entry, END, messagebox
from database.database import Database
from validation.validation import validate_author, validate_isbn

class BookApp:
    """Class representing the Book application."""

    def __init__(self, root):
        """Initialize BookApp instance."""
        self.root = root
        self.db = Database()
        self.create_main_window()

    def create_main_window(self):
        """Create the main window of the application."""
        self.title_label = Label(self.root, text="Title:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = Entry(self.root, width=30)
        self.title_entry.grid(row=0, column=1)

        self.author_label = Label(self.root, text="Author:")
        self.author_label.grid(row=1, column=0)
        self.author_entry = Entry(self.root, width=30)
        self.author_entry.grid(row=1, column=1)

        self.isbn_label = Label(self.root, text="ISBN:")
        self.isbn_label.grid(row=2, column=0)
        self.isbn_entry = Entry(self.root, width=30)
        self.isbn_entry.grid(row=2, column=1)

        self.submit_btn = Button(self.root, text="Submit", command=self.submit)
        self.submit_btn.grid(row=3, column=0, columnspan=2)

        self.show_books_btn = Button(self.root, text="Show Books", command=self.show_books)
        self.show_books_btn.grid(row=4, column=0, columnspan=2)

    def submit(self):
        """Submit a book entry to the database."""
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()

        if not title or not author or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not validate_author(author) or not validate_isbn(isbn):
            return

        # Inserting data into the database
        query = "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)"
        self.db.execute_query(query, (title, author, isbn))

        messagebox.showinfo("Success", "Book entry submitted successfully.")

        # Clearing the entry fields
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.isbn_entry.delete(0, END)

    def show_books(self):
        """Display all books stored in the database."""
        books = self.db.fetch_all("SELECT * FROM books")

        if not books:
            messagebox.showinfo("Information", "No books found in the database.")
            return

        # Creating a new window to display books
        show_books_window = Toplevel(self.root)
        show_books_window.title("Books List")

        for i, book in enumerate(books):
            for j, value in enumerate(book):
                label = Label(show_books_window, text=str(value))
                label.grid(row=i, column=j)

        # Adding a button to close the window
        close_btn = Button(show_books_window, text="Close", command=show_books_window.destroy)
        close_btn.grid(row=len(books), column=0, columnspan=len(book))

    def go_back(self):
        """Go back to the main screen."""
        # Go back functionality
        pass

    # Other methods like delete_book, edit_book, etc. can be added...
df