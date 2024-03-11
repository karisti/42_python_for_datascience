

def square(x: int | float) -> int | float:
    """
    Returns the square of the input

    Parameters:
        x (int | float): The number to square.

    Returns:
        int | float: The square of the input.
    """

    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns the power of the input to itself

    Parameters:
        x (int | float): The number to power.

    Returns:
        int | float: The power of the input to itself.
    """

    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an object that when called returns the result of the function

    Parameters:
        x (int | float): The number to calculate.
        function (function): The function to use for the calculation.

    Returns:
        object: The object that when called returns the result of the function.
    """

    count = 0

    try:
        assert isinstance(x, (int, float)), "x must be int or float"
        assert callable(function), "function must be callable"

        def inner() -> float:

            nonlocal x
            nonlocal count

            x = function(x)
            count += 1

            return x

        return inner

    except AssertionError as e:
        print("AssertionError:", e)
        return None
