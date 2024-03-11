import numpy as np


def get_numpy_2d_array(family: list) -> np.ndarray:
    """
    This function takes a 2D list and returns a numpy array.

    Parameters:
        family (list): A 2D list of integers or floats

    Returns:
        np.ndarray: A numpy array

    Raises:
        AssertionError:
            If family is not a list
            If family is not a 2D list,
            If family contains elements that are not lists
            If the lists in family are not of the same length
    """

    assert isinstance(family, list), "family must be a list"
    assert all(isinstance(f, list) and
               len(f) == len(family[0]) for f in family), \
           "all rows must be lists of the same length"

    np_family_array = np.array(family)

    assert len(np_family_array.shape) == 2, "Input must be a 2D list"

    return np_family_array


def slice_2d_array(np_array: np.ndarray, start: int, end: int) -> np.ndarray:
    """
    This function takes a numpy array and two indices, and returns a new numpy
    array containing the rows from start to end.

    Parameters:
        np_array (np.ndarray): A numpy array
        start (int): An integer representing the start index
        end (int): An integer representing the end index

    Returns:
        np.ndarray: A new numpy array containing the rows from start to end

    Raises:
        AssertionError:
            If start and end are not integers
    """

    assert isinstance(start, int) and isinstance(end, int), \
           "start and end must be integers"

    sliced_array = np_array[start:end]

    return sliced_array


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes a 2D list and two indices, and returns a new 2D list
    containing the rows from start to end.

    Parameters:
        family (list): A 2D list of integers or floats
        start (int): An integer representing the start index
        end (int): An integer representing the end index

    Returns:
        list: A new 2D list containing the rows from start to end
    """

    try:
        np_family_array = get_numpy_2d_array(family)

        print("My shape is :", np_family_array.shape)

        sliced_array = slice_2d_array(np_family_array, start, end)

        print("My new shape is :", sliced_array.shape)

        return sliced_array.tolist()

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
