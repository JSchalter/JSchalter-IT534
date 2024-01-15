# validator.py

class Validator:
    """
    Provides static methods for input validation.

    Methods:
    - check_invalid_chars(user_input, invalid_chars): 
        Checks if user input contains any invalid characters.
    - validate_student_id(student_id): 
        Validates the format of a student ID.
    - validate_name(name): 
        Validates the format of a person's name.
    - validate_email(email): 
        Validates the format of an email address.
    - validate_program_of_study(program_of_study): 
        Validates the format of a program of study.
    - validate_instructor_id(instructor_id): 
        Validates the format of an instructor ID.
    - validate_last_institution(last_institution): 
        Validates the format of the last institution where an instructor was affiliated.
    - validate_highest_degree(highest_degree): 
        Validates the format of the highest degree obtained by an instructor.
    - validate_individual_type(individual_type): 
        Validates the format of an individual's type.
    """
    @staticmethod
    def check_invalid_chars(user_input, invalid_chars):
        """
        Checks if user input contains any invalid characters.

        Parameters:
        - user_input (str): The user input to be checked.
        - invalid_chars (str): A string containing invalid characters.

        Returns:
        - bool: True if there are invalid characters, False otherwise.
        """
        for char in invalid_chars:
            if char in user_input:
                return True
        return False

    @staticmethod
    def validate_student_id(student_id):
        """
        Validates the format of a student ID.

        Parameters:
        - student_id (str): The student ID to be validated.

        Returns:
        - bool: True if the student ID is valid, False otherwise.
        """
        return student_id.isdigit() and len(student_id) <= 7
    
    @staticmethod
    def validate_name(name):
        """
        Validates the format of a person's name.

        Parameters:
        - name (str): The name to be validated.

        Returns:
        - bool: True if the name is valid, False otherwise.
        """
        return name.strip() != ""

    @staticmethod
    def validate_email(email):
        """
        Validates the format of an email address.

        Parameters:
        - email (str): The email address to be validated.

        Returns:
        - bool: True if the email address is valid, False otherwise.
        """
        return email.strip() != "" 

    @staticmethod
    def validate_program_of_study(program_of_study):
        """
        Validates the format of a program of study.

        Parameters:
        - program_of_study (str): The program of study to be validated.

        Returns:
        - bool: True if the program of study is valid, False otherwise.
        """
        return program_of_study.strip() != ""

    @staticmethod
    def validate_instructor_id(instructor_id):
        """
        Validates the format of an instructor ID.

        Parameters:
        - instructor_id (str): The instructor ID to be validated.

        Returns:
        - bool: True if the instructor ID is valid, False otherwise.
        """
        return instructor_id.isdigit() and len(instructor_id) <= 5

    @staticmethod
    def validate_last_institution(last_institution):
        """
        Validates the format of the last institution where an instructor was affiliated.

        Parameters:
        - last_institution (str): The last institution to be validated.

        Returns:
        - bool: True if the last institution is valid, False otherwise.
        """
        return last_institution.strip() != ""
    
    @staticmethod
    def validate_highest_degree(highest_degree):
        """
        Validates the format of the highest degree obtained by an instructor.

        Parameters:
        - highest_degree (str): The highest degree to be validated.

        Returns:
        - bool: True if the highest degree is valid, False otherwise.
        """
        return highest_degree.strip() != ""
    
    @staticmethod
    def validate_individual_type(individual_type):
        """
        Validates the format of an individual's type.

        Parameters:
        - individual_type (str): The individual's type to be validated.

        Returns:
        - bool: True if the individual's type is valid, False otherwise.
        """
        return individual_type.strip() != ""
