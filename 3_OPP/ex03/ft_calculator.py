

class calculator:
    """
    This class is a simple calculator that can add, multiply,
    substract and divide by a number each number of a list.
    """

    def __init__(self, l_numbers) -> None:
        """
        This method initializes the list of numbers.

        Parameters:
            l_numbers (list): List of numbers.
        """

        self.l_numbers = l_numbers

    def __add__(self, object) -> None:
        """
        This method adds the given object to each number
        of the list and prints the result list.

        Parameters:
            object (int): Number to add to each number of the list.

        Returns:
            None
        """

        self.l_numbers = [number + object for number in self.l_numbers]

        print(self.l_numbers)

    def __mul__(self, object) -> None:
        """
        This method multiplies each number of the list
        by the given object and prints the result list.

        Parameters:
            object (int): Number to multiply each number of the list by.

        Returns:
            None
        """

        self.l_numbers = [number * object for number in self.l_numbers]

        print(self.l_numbers)

    def __sub__(self, object) -> None:
        """
        This method substracts the given object from each number
        of the list and prints the result list.

        Parameters:
            object (int): Number to substract from each number of the list.

        Returns:
            None
        """

        self.l_numbers = [number - object for number in self.l_numbers]

        print(self.l_numbers)

    def __truediv__(self, object) -> None:
        """
        This method divides each number of the list by the given
        object and prints the result list.

        Parameters:
            object (int): Number to divide each number of the list by.

        Returns:
            None
        """

        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero not allowed.")

            self.l_numbers = [number / object for number in self.l_numbers]

            print(self.l_numbers)

        except ZeroDivisionError as e:
            print("ZeroDivisionError:", e)
