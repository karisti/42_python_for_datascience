from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Baratheon constructor method. Initializes first_name,
        is_alive, family_name, eyes and hairs attributes.

        Parameters:
            first_name (str): Baratheon first name.
            is_alive (bool): Baratheon status. Optional. Default is True.
        """

        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be bool"

            self.first_name = first_name
            self.is_alive = is_alive
            self.family_name = "Baratheon"
            self.eyes = "brown"
            self.hairs = "dark"

        except AssertionError as e:
            print("AssertionError:", e)

    def die(self):
        """
        Baratheon die method. Changes is_alive to False.

        Parameters:
            None

        Returns:
            None
        """

        self.is_alive = False

    def __str__(self):
        """
        Baratheon __str__ method. Returns a string representation
        of the object.

        Parameters:
            None

        Returns:
            str: String representation of the object.
        """

        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """
        Baratheon __repr__ method. Returns a string representation
        of the object.

        Parameters:
            None

        Returns:
            str: String representation of the object.
        """

        return f"Vector: {self.family_name, self.eyes, self.hairs}"


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Lannister constructor method. Initializes first_name,
        is_alive, family_name, eyes and hairs attributes.

        Parameters:
            first_name (str): Lannister first name.
            is_alive (bool): Lannister status. Optional. Default is True.
        """

        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be bool"

            self.first_name = first_name
            self.is_alive = is_alive
            self.family_name = "Lannister"
            self.eyes = "blue"
            self.hairs = "light"

        except AssertionError as e:
            print("AssertionError:", e)

    def die(self):
        """
        Lannister die method. Changes is_alive to False.

        Parameters:
            None

        Returns:
            None
        """

        self.is_alive = False

    @classmethod
    def create_lannister(self, name, is_alive=True):
        """
        Lannister create_lannister method. Creates a Lannister object.

        Parameters:
            name (str): Lannister first name.
            is_alive (bool): Lannister status. Optional. Default is True.

        Returns:
            Lannister: A Lannister object.
        """

        return Lannister(name, is_alive)

    def __str__(self):
        """
        Lannister __str__ method. Returns a string representation

        Parameters:
            None

        Returns:
            str: String representation of the object.
        """

        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """
        Lannister __repr__ method. Returns a string representation
        of the object.

        Parameters:
            None

        Returns:
            str: String representation of the object.
        """

        return f"Vector: {self.family_name, self.eyes, self.hairs}"
