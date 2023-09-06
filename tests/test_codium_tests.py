import numpy as np
from source.clean_01 import cleanup_tuple


def test_cleanup_tuple_with_string_and_float():
    # Arrange
    tup = ('Title', 3.14)

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert result == 'Title, 3.0%'


def test_cleanup_tuple_with_string_and_integer():
    # Arrange
    tup = ('Title', 5)

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert result == 'Title, 5.0%'


def test_cleanup_tuple_with_string_and_negative_float():
    # Arrange
    tup = ('Title', -2.5)

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert result == 'Title, -2.0%'


def test_cleanup_tuple_with_string_and_float_with_decimal_places():
    # Arrange
    tup = ('Title', 2.75)

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert result == 'Title, 3.0%'


def test_cleanup_tuple_with_string_and_float_with_large_number_of_decimal_places():
    # Arrange
    tup = ('Title', 2.999999999999999)

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert result == 'Title, 3.0%'


def test_cleanup_tuple_with_none_as_input():
    # Arrange
    tup = None

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert np.isnan(result)

def test_cleanup_tuple_with_string_and_float():
    # Arrange
    tup = ('title', 100.0)

    # Act
    result = cleanup_tuple(tup)

    # Assert
    assert result == 'title, 100.0%'