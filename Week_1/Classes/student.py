# student.py
from Classes.person import Person

class Student(Person):
    """
    Represents a Student, inheriting from the Person class.

    Attributes:
    - name (str): The name of the student.
    - email (str): The email address of the student.
    - student_id (int): The unique identifier for the student.
    - program_of_study (str): The program of study in which the student is enrolled.

    Methods:
    - __init__(self, name, email, student_id, program_of_study): 
        Initializes a new instance of the Student class.
    - display_information(self): 
        Displays information about the student, including inherited information from the Person class.
    """
    def __init__(self, name, email, student_id, program_of_study):
        """
        Initializes a new instance of the Student class.

        Parameters:
        - name (str): The name of the student.
        - email (str): The email address of the student.
        - student_id (int): The unique identifier for the student.
        - program_of_study (str): The program of study in which the student is enrolled.
        """
        super().__init__(name, email)
        self.student_id = student_id
        self.program_of_study = program_of_study

    def display_information(self):
        """
        Displays information about the student, including inherited information from the Person class.
        """
        super().display_information()
        print(f"Student ID: {self.student_id}\nProgram of Study: {self.program_of_study}\n")
