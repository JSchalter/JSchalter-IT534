import Functions.helpers as helpers
from Classes.variable_sorter import VariableSort

if __name__ == "__main__":
    sorter = VariableSort()

    while True:
        # Prompt user for a string
        while True:
            try:
                user_input = input("Enter a string: ")
                value = str(user_input)
                sorter.validate_and_sort(value)
                break  # Move to the next input type after successful input

            except ValueError as error:
                print(f"Error: {error}")

        # Prompt user for an integer
        while True:
            try:
                user_input = input("Enter an integer: ")
                value = int(user_input)
                sorter.validate_and_sort(value)
                break  # Move to the next input type after successful input

            except ValueError as error:
                print(f"Error: {error}")

        # Prompt user for a float
        while True:
            try:
                user_input = input("Enter a float: ")
                value = float(user_input)
                sorter.validate_and_sort(value)
                break  # Exit the loop after successful input

            except ValueError as error:
                print(f"Error: {error}")

        # Ask if the user wants to input more data
        more_data = input("Do you want to input more data? (yes/no): ").lower()
        if more_data != 'yes':
            break  # Exit the loop if the user says no

    # Display the sorted lists
    print(f"Strings: {sorter.strings}")
    print(f"Integers: {sorter.integers}")
    print(f"Floats: {sorter.floats}")