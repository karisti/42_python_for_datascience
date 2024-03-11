

def callLimit(limit: int):
    """
    This function is a decorator that limits the amount of times a function
    can be called.

    Parameters:
        limit (int): The amount of times the function can be called.

    Returns:
        function: The function that limits the amount of times a function
        can be called.
    """

    count = 0

    def callLimiter(function):
        """
        This function returns a function that limits the amount of times
        a function can be called.

        Parameters:
            function (function): The function to be called.

        Returns:
            function: The function that limits the amount of times a function
            can be called.
        """

        def limit_function(*args: any, **kwds: any):
            """
            This function limits the amount of times a function can be called.
            It returns the result of the function if it is called less times
            than the limit, otherwise it prints an error message.

            Parameters:
                *args (any): The arguments of the function.
                **kwds (any): The keyword arguments of the function.

            Returns:
                any: The result of the function if it is called less times than
                the limit, otherwise it prints an error message.
            """

            try:
                nonlocal count

                assert limit > 0, "Error: limit must be greater than 0"
                assert count < limit, f"Error: {function} call too many times"

                count += 1

                return function(*args, **kwds)

            except AssertionError as e:
                print(e)
                return None

        return limit_function

    return callLimiter
