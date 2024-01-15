# person.py

class Person:
    """
    Represents a Person with basic information.

    Attributes:
    - name (str): The name of the person.
    - email (str): The email address of the person.

    Methods:
    - __init__(self, name, email): 
        Initializes a new instance of the Person class.
    - display_information(self): 
        Displays basic information about the person.
    """
    def __init__(self, name, email):
        """
        Initializes a new instance of the Person class.

        Parameters:
        - name (str): The name of the person.
        - email (str): The email address of the person.
        """
        self.name = name
        self.email = email

    def display_information(self):
        """
        Displays basic information about the person.
        """
        print(f"Name: {self.name}\nEmail: {self.email}")
