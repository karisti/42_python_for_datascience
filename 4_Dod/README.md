## 4. Dod

### Ex00
- `*args` variable length argument list.
- `**kwargs` variable length keyword argument list.

**Statistics**

| Statistic   | Explanation                                         | Example Use Case                                       | Calculation                                |
|-------------|-----------------------------------------------------|--------------------------------------------------------|--------------------------------------------|
| Mean        | The arithmetic average of a set of numbers.         | Calculating the average score in a class.              | Add up all numbers and divide by the count of numbers.        |
| Median      | The middle value in a sorted list of numbers.       | Finding the median income in a dataset.               | Arrange numbers in ascending order and find the middle value. If even, average the two middle values. |
| Quartile    | Values that divide a dataset into four equal parts. | Analyzing income distribution in a population.        | Sort data, then find the median of the lower half (Q1), median (Q2), and median of the upper half (Q3). |
| Variance    | A measure of how spread out the numbers are.        | Assessing the variability of stock returns.           | Find the average of squared differences between each number and the mean. |
| Standard deviation     | The square root of the variance.                    | Understanding the volatility of a portfolio.          | Calculate the square root of the variance. |


### Ex01
A function can return a function. :D

- `nonlocal` allows to use a variable of an outer scope.
- `callable(function)` allows to check if function is a function.


### Ex02
Creating a decorator.

It needs 3 function levels if decorator has argument `@callLimit(3)`, 2 if not.
- 1st level: decorator args.
- 2nd level: function to execute.
- 3rd level: args for function to execute.

```
def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):

            try:
                nonlocal count
                count += 1
                return function(*args, **kwds)

        return limit_function

    return callLimiter
```

### Ex03
`dataclass` usage.

- `@dataclass` decorator in the class.
- Each attribute is a `field`. It has different possible arguments:
    - init (True / False): Allows user to give value or not.
    - default: Sets the default value for the field.
    - default_factory: Allows to call a factory function to generate the value.
- `__post_init__` can be used to do things after class initialization.



```
import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default="")
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.lower()
```
