def is_valid_string(value):
    """
    Check if the value is a valid string.

    Parameters:
    - value: Input value to be checked.

    Returns:
    - True if the value is a valid string, False otherwise.
    """
    return isinstance(value, str) and value.isalpha()

def is_valid_float(value):
    """
    Check if the value is a valid float.

    Parameters:
    - value: Input value to be checked.

    Returns:
    - True if the value is a valid float, False otherwise.
    """
    return isinstance(value, float)

def is_valid_integer(value):
    """
    Check if the value is a valid integer.

    Parameters:
    - value: Input value to be checked.

    Returns:
    - True if the value is a valid integer, False otherwise.
    """
    return isinstance(value, int)
