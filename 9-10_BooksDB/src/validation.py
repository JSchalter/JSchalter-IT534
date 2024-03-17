"""Module for validation functions."""

from tkinter import messagebox

def validate_author(author):
    """Validate author name."""
    if not author.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Author name must contain letters only")

def validate_isbn(isbn):
    """Validate ISBN."""
    if not isbn.isdigit():
        messagebox.showerror("Error", "ISBN must contain numbers only")

def validate_copies_purchased(copies_purchased):
    """Validate copies purchased."""
    try:
        int(copies_purchased)
    except ValueError:
        messagebox.showerror("Error", "Copies purchased must be an integer")

def validate_copies_not_checked_out(copies_not_checked_out):
    """Validate copies not checked out."""
    try:
        int(copies_not_checked_out)
    except ValueError:
        messagebox.showerror("Error", "Copies not checked out must be an integer")

def validate_retail_price(retail_price):
    """Validate retail price."""
    try:
        float(retail_price)
    except ValueError:
        messagebox.showerror("Error", "Retail price must be a float value")
