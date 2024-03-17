from tkinter import messagebox

def validate_author(author):
    """
    Validate author name.

    Args:
        author (str): Author name to be validated.

    Returns:
        bool: True if author name is valid, False otherwise.
    """
    if not author.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Author name must contain letters only")
        return False
    return True

def validate_isbn(isbn):
    """
    Validate ISBN.

    Args:
        isbn (str): ISBN to be validated.

    Returns:
        bool: True if ISBN is valid, False otherwise.
    """
    if not isbn.isdigit():
        messagebox.showerror("Error", "ISBN must contain numbers only")
        return False
    return True

# Other validation functions can be similarly defined...
