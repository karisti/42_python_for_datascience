

class calculator:
    """
    This class is another simple calculator that can calculate
    the dot product, the sum and the difference of two vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        This method calculates the dot product of two vectors
        and prints the result.

        Parameters:
            V1 (list): First vector.
            V2 (list): Second vector.

        Returns:
            None
        """

        result = 0

        for x, y in zip(V1, V2):
            result += x * y

        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        This method calculates the sum of two vectors
        and prints the result.

        Parameters:
            V1 (list): First vector.
            V2 (list): Second vector.

        Returns:
            None
        """

        result = [float(x + y) for x, y in zip(V1, V2)]

        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        This method calculates the difference of two vectors
        and prints the result.

        Parameters:
            V1 (list): First vector.
            V2 (list): Second vector.

        Returns:
            None
        """

        result = [float(x - y) for x, y in zip(V1, V2)]

        print(f"Sous Vector is: {result}")
