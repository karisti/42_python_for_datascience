from abc import ABC, abstractmethod


class Character(ABC):
    """
    Character abstract class.

    Attributes:
        first_name (str): Character first name.
        is_alive (bool): Character status.

    Methods:
        __init__: Character constructor method.
        die: Character die method.
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Character constructor method. Must initialize first_name
        and is_alive attributes.

        Parameters:
            first_name (str): Character first name.
            is_alive (bool): Character status. Optional. Default is True.
        """

        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be boolean"

            self.first_name = first_name
            self.is_alive = is_alive

        except AssertionError as e:
            print("AssertionError:", e)

    @abstractmethod
    def die(self):
        """
        Character die method. Must change is_alive to False.

        Parameters:
            None

        Returns:
            None
        """

        self.is_alive = False


class Stark(Character):
    """
    Stark class. Inherits from Character class.

    Attributes:
        first_name (str): Stark first name.
        is_alive (bool): Stark status.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Stark constructor method. Initializes first_name and
        is_alive attributes.

        Parameters:
            first_name (str): Stark first name.
            is_alive (bool): Stark status. Optional. Default is True.
        """

        super().__init__(first_name, is_alive)

    def die(self):
        """
        Stark die method. Changes is_alive to False.

        Parameters:
            None
        """

        super().die()
