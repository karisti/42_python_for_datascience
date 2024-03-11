from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family."""

    def __init__(self, first_name, is_alive=True):
        """
        King constructor method. Initializes first_name and is_alive
        attributes.

        Parameters:
            first_name (str): First name of the King.
            is_alive (bool): Is the King alive or not.
        """

        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, eyes):
        """
        King set_eyes method. Changes eyes attribute
        to the given value.

        Parameters:
            eyes (str): King eyes color.

        Returns:
            None
        """

        try:
            assert isinstance(eyes, str), \
                "eyes attribute must be a string."

            self.eyes = eyes

        except AssertionError as e:
            print("AssertionError:", e)

    def get_eyes(self):
        """
        King get_eyes method. Returns eyes attribute.

        Parameters:
            None

        Returns:
            str: King eyes color.
        """

        return self.eyes

    def set_hairs(self, hairs):
        """
        King set_hairs method. Changes hairs attribute
        to the given value.

        Parameters:
            hairs (str): King hairs color.

        Returns:
            None
        """

        try:
            assert isinstance(hairs, str), \
                "hairs attribute must be a string."

            self.hairs = hairs

        except AssertionError as e:
            print("AssertionError:", e)

    def get_hairs(self):
        """
        King get_hairs method. Returns hairs attribute.

        Parameters:
            None

        Returns:
            str: King hairs color.
        """

        return self.hairs
