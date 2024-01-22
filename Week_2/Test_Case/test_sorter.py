def test_sorter():
    """Test the VariableSort class by validating and sorting different types of values."""
    sorter = VariableSort()

    # Test string values
    test_str_value = "abc"
    sorter.validate_and_sort(test_str_value)
    assert sorter.strings == [test_str_value]

    # Test integer values
    test_int_value = 42
    sorter.validate_and_sort(test_int_value)
    assert sorter.integers == [test_int_value]

    # Test float values
    test_float_value = 3.14
    sorter.validate_and_sort(test_float_value)
    assert sorter.floats == [test_float_value]

    # Test invalid data type
    try:
        sorter.validate_and_sort(True)
    except ValueError as error:
        assert str(error) == "Invalid data type for value: True"
    else:
        assert False, "Expected ValueError for invalid data type"
