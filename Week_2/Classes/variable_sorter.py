import Functions.helpers as helpers

class VariableSort:
    """Sorts variables into lists based on their type."""

    def __init__(self):
        """Initialize with lists for string, float, and integer values."""
        self.strings = []  # List for string values
        self.floats = []   # List for float values
        self.integers = []  # List for integer values

    def validate_and_sort(self, value):
        """
        Validate data type and sort value into the appropriate list.

        Parameters:
        - value: Input value to be sorted.
        """
        if helpers.is_valid_string(value):
            self.strings.append(value)
        elif helpers.is_valid_float(value):
            self.floats.append(value)
        elif helpers.is_valid_integer(value):
            self.integers.append(value)
        else:
            raise ValueError(f"Invalid data type for value: {value}")