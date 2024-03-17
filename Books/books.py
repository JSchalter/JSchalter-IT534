from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import simpledialog

# Function to validate author name
def ValidateAuthor():
    passed_author = author.get()
    if not passed_author.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Author name must contain letters only")

# Function to validate ISBN
def ValidateISBN():
    passed_isbn = isbn.get()
    if not passed_isbn.isdigit():
        messagebox.showerror("Error", "ISBN must contain numbers only")

# Function to validate copies purchased
def ValidateCopiesPurchased():
    passed_copies_purchased = copies_purchased.get()
    try:
        int(passed_copies_purchased)
    except ValueError:
        messagebox.showerror("Error", "Copies purchased must be an integer")

# Function to validate copies not checked out
def ValidateCopiesNotCheckedOut():
    passed_copies_not_checked_out = copies_not_checked_out.get()
    try:
        int(passed_copies_not_checked_out)
    except ValueError:
        messagebox.showerror("Error", "Copies not checked out must be an integer")

# Function to validate retail price
def ValidateRetailPrice():
    passed_retail_price = retail_price.get()
    try:
        float(passed_retail_price)
    except ValueError:
        messagebox.showerror("Error", "Retail price must be a float value")

# Function to add a book
def submit(root):  # Pass root as an argument
    ValidateAuthor()
    ValidateISBN()
    ValidateCopiesPurchased()
    ValidateCopiesNotCheckedOut()
    ValidateRetailPrice()

    conn = sqlite3.connect('Books.db')
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?, ?)",
              (
                  title.get(),
                  author.get(),
                  isbn.get(),
                  copies_purchased.get(),
                  copies_not_checked_out.get(),
                  retail_price.get()
              )
              )
    conn.commit()
    conn.close()

    # Clearing Entry widgets
    title.delete(0, END)
    author.delete(0, END)
    isbn.delete(0, END)
    copies_purchased.delete(0, END)
    copies_not_checked_out.delete(0, END)
    retail_price.delete(0, END)

# Function to confirm if the user wants to go back to the main screen
def go_back():
    response = messagebox.askyesno("Confirmation", "Are you sure you want to go back to the main screen?")
    if response:
        root.deiconify()  # Show the main window
        show_books_window.destroy()  # Close the "Show Books" window

# Function to delete a book
def delete(book_id):
    response = messagebox.askyesno("Confirmation", "Are you sure you want to delete this book?")
    if response == 1:
        conn = sqlite3.connect('Books.db')
        c = conn.cursor()
        c.execute("DELETE from books WHERE book_id = ?", (book_id,))
        conn.commit()
        conn.close()
        show_books()

# Function to display all books
def show_books():
    global show_books_window
    show_books_window = Toplevel(root)
    show_books_window.title("Books List")
    show_books_window.geometry("600x500")

    # Go Back Button
    go_back_btn = Button(show_books_window, text="Go Back", command=go_back)
    go_back_btn.grid(row=0, column=0, columnspan=2, sticky="nw")

    conn = sqlite3.connect('Books.db')
    c = conn.cursor()

    c.execute("SELECT * FROM books")
    books = c.fetchall()

    # Clear previous results before displaying new ones
    for widget in show_books_window.winfo_children():
        if isinstance(widget, Label) or isinstance(widget, Entry) or isinstance(widget, Button):
            widget.destroy()

    row_num = 1
    for book in books:
        title_label = Label(show_books_window, text="Title:")
        title_label.grid(row=row_num, column=0)
        title_value = Label(show_books_window, text=book[1])
        title_value.grid(row=row_num, column=1)

        author_label = Label(show_books_window, text="Author:")
        author_label.grid(row=row_num+1, column=0)
        author_value = Label(show_books_window, text=book[2])
        author_value.grid(row=row_num+1, column=1)

        isbn_label = Label(show_books_window, text="ISBN:")
        isbn_label.grid(row=row_num+2, column=0)
        isbn_value = Label(show_books_window, text=book[3])
        isbn_value.grid(row=row_num+2, column=1)

        copies_purchased_label = Label(show_books_window, text="Copies Purchased:")
        copies_purchased_label.grid(row=row_num+3, column=0)
        copies_purchased_value = Label(show_books_window, text=book[4])
        copies_purchased_value.grid(row=row_num+3, column=1)

        copies_not_checked_out_label = Label(show_books_window, text="Copies Not Checked Out:")
        copies_not_checked_out_label.grid(row=row_num+4, column=0)
        copies_not_checked_out_value = Label(show_books_window, text=book[5])
        copies_not_checked_out_value.grid(row=row_num+4, column=1)

        retail_price_label = Label(show_books_window, text="Retail Price:")
        retail_price_label.grid(row=row_num+5, column=0)
        retail_price_value = Label(show_books_window, text=book[6])
        retail_price_value.grid(row=row_num+5, column=1)

        book_id_label = Label(show_books_window, text="Book ID:")
        book_id_label.grid(row=row_num+6, column=0)
        book_id_value = Label(show_books_window, text=book[0])
        book_id_value.grid(row=row_num+6, column=1)

        edit_btn = Button(show_books_window, text="Edit", command=lambda id=book[0]: edit_book(id))
        edit_btn.grid(row=row_num+7, column=0)

        delete_btn = Button(show_books_window, text="Delete", command=lambda id=book[0]: delete(id))
        delete_btn.grid(row=row_num+7, column=1)

        # Insert blank line
        blank_line = Label(show_books_window, text="")
        blank_line.grid(row=row_num+8, column=0, columnspan=2)

        row_num += 9

    conn.close()

# Function to edit a book
def edit_book(book_id):
    conn = sqlite3.connect('Books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE book_id=?", (book_id,))
    book_record = c.fetchone()
    conn.close()
    if book_record:
        # Creating a new window for editing
        edit_window = Toplevel(root)
        edit_window.title("Edit Book")
        edit_window.geometry("300x200")

        def submit_edit():
            response = messagebox.askyesno("Confirmation", "Do you want to save the changes?")
            if response:
                conn = sqlite3.connect('Books.db')
                c = conn.cursor()
                c.execute("UPDATE books SET title=?, author=?, isbn=?, copies_purchased=?, copies_not_checked_out=?, retail_price=? WHERE book_id=?",
                          (title_edit.get(), author_edit.get(), isbn_edit.get(), copies_purchased_edit.get(), copies_not_checked_out_edit.get(), retail_price_edit.get(), book_id))
                conn.commit()
                conn.close()
                edit_window.destroy()
                show_books()

        title_edit_label = Label(edit_window, text="Title:")
        title_edit_label.grid(row=0, column=0)
        title_edit = Entry(edit_window, width=30)
        title_edit.grid(row=0, column=1)
        title_edit.insert(0, book_record[1])

        author_edit_label = Label(edit_window, text="Author:")
        author_edit_label.grid(row=1, column=0)
        author_edit = Entry(edit_window, width=30)
        author_edit.grid(row=1, column=1)
        author_edit.insert(0, book_record[2])

        isbn_edit_label = Label(edit_window, text="ISBN:")
        isbn_edit_label.grid(row=2, column=0)
        isbn_edit = Entry(edit_window, width=30)
        isbn_edit.grid(row=2, column=1)
        isbn_edit.insert(0, book_record[3])

        copies_purchased_edit_label = Label(edit_window, text="Copies Purchased:")
        copies_purchased_edit_label.grid(row=3, column=0)
        copies_purchased_edit = Entry(edit_window, width=30)
        copies_purchased_edit.grid(row=3, column=1)
        copies_purchased_edit.insert(0, book_record[4])

        copies_not_checked_out_edit_label = Label(edit_window, text="Copies Not Checked Out:")
        copies_not_checked_out_edit_label.grid(row=4, column=0)
        copies_not_checked_out_edit = Entry(edit_window, width=30)
        copies_not_checked_out_edit.grid(row=4, column=1)
        copies_not_checked_out_edit.insert(0, book_record[5])

        retail_price_edit_label = Label(edit_window, text="Retail Price:")
        retail_price_edit_label.grid(row=5, column=0)
        retail_price_edit = Entry(edit_window, width=30)
        retail_price_edit.grid(row=5, column=1)
        retail_price_edit.insert(0, book_record[6])

        submit_edit_btn = Button(edit_window, text="Submit", command=submit_edit)
        submit_edit_btn.grid(row=6, column=0, columnspan=2)

    else:
        messagebox.showerror("Error", "Book ID not found")

# Main window
root = Tk()
root.title('Books Database')
root.geometry("1000x500")

# Entry widgets for user input
title = Entry(root, width=30)
title.grid(row=0, column=1)

author = Entry(root, width=30)
author.grid(row=2, column=1)

isbn = Entry(root, width=30)
isbn.grid(row=3, column=1)

copies_purchased = Entry(root, width=30)
copies_purchased.grid(row=4, column=1)

copies_not_checked_out = Entry(root, width=30)
copies_not_checked_out.grid(row=5, column=1)

retail_price = Entry(root, width=30)
retail_price.grid(row=6, column=1)

delete_book = Entry(root, width=30)
delete_book.grid(row=7, column=1)

# Labels for entry widgets
title_label = Label(root, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(root, text="Author")
author_label.grid(row=2, column=0)

isbn_label = Label(root, text="ISBN")
isbn_label.grid(row=3, column=0)

copies_purchased_label = Label(root, text="Copies Purchased")
copies_purchased_label.grid(row=4, column=0)

copies_not_checked_out_label = Label(root, text="Copies Not Checked Out")
copies_not_checked_out_label.grid(row=5, column=0)

retail_price_label = Label(root, text="Retail Price")
retail_price_label.grid(row=6, column=0)

delete_book_label = Label(root, text="Book ID")
delete_book_label.grid(row=7, column=0)

# Buttons for actions
submit_btn = Button(root, text="Add Book", command=lambda: submit(root))
submit_btn.grid(row=8, column=0)

query_btn = Button(root, text="Show Books", command=show_books)
query_btn.grid(row=9, column=0)

# Main loop for the Tkinter window
root.mainloop()
