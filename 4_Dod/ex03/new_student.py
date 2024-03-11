import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student.

    Attributes:
        name (str): The name of the student.
        surname (str): The surname of the student.
        active (bool): Indicates if the student is active. Default is True.
        login (str): The login of the student.
        id (str): The ID of the student.

    Methods:
        __post_init__(self): Initializes the login attribute.
    """

    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default="")
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Initializes the login attribute.

        Parameters:
            self (Student): The Student object.

        Returns:
            None
        """

        try:
            assert len(self.name) > 0, "Name cannot be empty"
            assert len(self.surname) > 0, "Surname cannot be empty"

            self.login = self.name[0].upper() + self.surname.lower()

        except AssertionError as e:
            print("AssertionError:", e)
