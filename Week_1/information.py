# information.py
from Classes.validator import Validator
from Classes.student import Student
from Classes.instructor import Instructor

def get_student_info():
    """
    Collects and validates information for a student.

    Returns:
    - Tuple[str, str]: A tuple containing student_id and program_of_study.
    """
    while True:
        student_id = input("Enter your Student ID: ")
        if not Validator.validate_student_id(student_id):
            print("Enter a valid Student ID")
        else:
            program_of_study = input("Enter your Program of Study: ")
            if not Validator.validate_program_of_study(program_of_study):
                print("Enter a valid program")
                continue
            else:
                break
    
    return student_id, program_of_study

def get_instructor_info():
    """
    Collects and validates information for an instructor.

    Returns:
    - Tuple[str, str, str]: A tuple containing instructor_id, last_institution, and highest_degree.
    """
    while True:
        instructor_id = input("Enter your Instructor ID: ")
        if not Validator.validate_instructor_id(instructor_id):
            print("Enter a valid Instructor ID")
        else:
            last_institution = input("Enter the Last Institution you graduated from: ")
            if not Validator.validate_last_institution(last_institution):
                print("Enter a valid institution")
            else: 
                highest_degree = input("Enter your Highest Degree earned: ")
                if not Validator.validate_highest_degree(highest_degree):
                    print("Enter your highest degree")
                else:
                    break
                
    return instructor_id, last_institution, highest_degree

def gather_information():
    """
    Gathers information about individuals (instructors or students) and creates records.

    Displays the collected information in college records.
    """
    college_records = []

    while True:
        individual_type = input("What type of individual are you? (instructor/student): ").lower()
        if not Validator.validate_individual_type(individual_type):
            print("You must select an individual type to use this application! Please re-enter.")
            continue

        name = input("Enter your Name: ")
        if not Validator.validate_name(name):
            print("You must enter a name")
            continue

        email = input("Enter your Email: ")
        if not Validator.validate_email(email):
            print("You must enter an email")
            continue

        if Validator.check_invalid_chars(name, ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']):
            print("Invalid characters in name. Please re-enter.")
            continue

        if Validator.check_invalid_chars(email, ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']):
            print("Invalid characters in email. Please re-enter.")
            continue

        if individual_type == 'instructor':
            instructor_id, last_institution, highest_degree = get_instructor_info()
            individual = Instructor(name, email, instructor_id, last_institution, highest_degree)
        elif individual_type == 'student':
            student_id, program_of_study = get_student_info()
            individual = Student(name, email, student_id, program_of_study)
        else:
            print("Invalid input. Please enter 'instructor' or 'student'.")
            continue

        college_records.append(individual)

        more_records = input("Would you like to enter more records? (yes/no): ").lower()
        if more_records != 'yes':
            break

    print("\nCollege Records:\n")
    for record in college_records:
        record.display_information()
        print()

# Run the function to gather information
gather_information()

