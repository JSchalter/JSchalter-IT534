# instructor.py
from Classes.person import Person

class Instructor(Person):
    """
    Represents an Instructor, inheriting from the Person class.

    Attributes:
    - name (str): The name of the instructor.
    - email (str): The email address of the instructor.
    - instructor_id (int): The unique identifier for the instructor.
    - last_institution (str): The last institution where the instructor was affiliated.
    - highest_degree (str): The highest degree obtained by the instructor.

    Methods:
    - __init__(self, name, email, instructor_id, last_institution, highest_degree): 
        Initializes a new instance of the Instructor class.
    - display_information(self): 
        Displays information about the instructor, including inherited information from the Person class.
    """
    def __init__(self, name, email, instructor_id, last_institution, highest_degree):
        """
        Initializes a new instance of the Instructor class.

        Parameters:
        - name (str): The name of the instructor.
        - email (str): The email address of the instructor.
        - instructor_id (int): The unique identifier for the instructor.
        - last_institution (str): The last institution where the instructor was affiliated.
        - highest_degree (str): The highest degree obtained by the instructor.
        """
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.last_institution = last_institution
        self.highest_degree = highest_degree
        
        """
        Displays information about the instructor, including inherited information from the Person class.
        """
        super().display_information()
        print(f"Instructor ID: {self.instructor_id}\nLast Institution: {self.last_institution}\nHighest Degree: {self.highest_degree}")
