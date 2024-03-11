## 3. OPP
Object 

### Ex00
Abstract class and inheritance. [See Abstract class in Python](https://www.scaler.com/topics/abstract-class-in-python/)

- Abstract methots (marked with `@abstractmethod`) need to be reimplemented by the classes that are going to inherit from that class.
- `super()` allows to call the implementation of the function of the parent.
```
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        self.is_alive = False

class Stark(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def die(self):
        super().die()
```

### Ex01
- Needs to reimplement the abstract methods from ex00.
- Implementes `__str__` to return str version of the class.
- Implements `__repr__` to return representation of the class.
- `@classmethod` is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like @staticmethod.

|                       | `classmethod`                                        | `staticmethod`                                         |
|-----------------------|-------------------------------------------------------|--------------------------------------------------------|
| **Definition**        | Method belonging to the class itself. Receives class as first argument.  | Method that does not receive an implicit first argument. |
| **Decorator**         | `@classmethod`                                       | `@staticmethod`                                        |
| **First Parameter**   | `cls` (conventionally named)                         | None                                                   |
| **Usage**             | Manipulating class-level variables, factory methods. | Utility functions, independent of instances or classes. |
| **Access to Variables**| Can access and modify class-level variables.         | Cannot access class or instance variables.             |


### Ex02
Multiple inheritance.

- A class that inherits from multiple classes can call any of the functions of them. Example: `Baratheon.__init__(self, first_name, is_alive)` calls `__init__ from Baratheon class`.

### Ex03
Operator overload.

- `__add__` for `+`
- `__sub__` for `-`
- `__mul__` for `*`
- `__truediv__` for `/`

### Ex04
Static methods (see ex01).
