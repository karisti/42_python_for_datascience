## 0. Starting

### Ex00
Non-Primitive data structures:
| Feature       | List                      | Tuple                     | Set                       | Dictionary                |
|---------------|---------------------------|---------------------------|---------------------------|---------------------------|
| **Definition**| Ordered collection of items | Ordered collection of items (immutable) | Unordered collection of unique items | Collection of key-value pairs |
| **Mutability**| Mutable                   | Immutable                 | Mutable                   | Mutable                   |
| **Indexing**  | Access by index           | Access by index           | No indexing               | Access by key             |
| **Duplicates**| Duplicates allowed        | Duplicates allowed        | No duplicates             | Duplicates not allowed    |
| **Syntax**    | `[ ]`                     | `( )`                     | `{ }`                     | `{ key: value }`          |
| **Example**   | `[1, 2, 'a', 'b']`       | `(1, 2, 'a', 'b')`        | `{1, 2, 'a', 'b'}`        | `{'a': 1, 'b': 2}`       |
| **Use case**  | When order matters and duplicates are allowed | When order matters and you want immutability | When uniqueness matters, and order or duplicates don't | When mapping keys to values |


### Ex01
Work with timestamps:
- `time.time()` gets current unix timestamp
- `time.strftime("%b %d %Y", time.localtime(timestamp))` allows to format the timestamp in the desired format.


### Ex02
Object type:
- `type(<object>)` returns the type of the object as `<class 'list'>`, `<class 'str'>`, etc.


### Ex03
Null types:
| Data Type     | Null Value                                  | How to Check                                                |
|---------------|---------------------------------------------|-------------------------------------------------------------|
| NoneType      | None                                        | `object is None`                                            |
| float         | NaN (Not a Number)                          | `object != object`            |
| int           | 0                                           | `object == 0`                   |
| str           | ''                                | `len(object) == 0`              |
| bool          | False                                       | `object is False`              |


### Ex04
- Get command line arguments with `sys.argv`. First argument is the program name.
- Raise exceptions with `raise <Exception>` and catch them in an `try-except block`.


### Ex05
- str has `isupper()`, `islower()`, `isspace()` and `isdigit()`
- Punctuation symbols: `"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"`
- Get user input: `input("Type input")`


### Ex06
- List comprehension: `new_list = [expression for item in iterable if condition]`
- Lambda: It allows you to create a function without a proper name (hence "anonymous") in a single line of code. `lambda arguments: expression`


### Ex07
Dictionary usage and str join.
- `dic_name['key']` takes value of key.
- `dic_name.keys()` gets the keys of the dict.
- `dic_name.values()` gets the values of the dict.
- `" ".join(list)` creates a string appending elements with " ".


### Ex08
- `yield` operator in Python is used within generator functions to generate a sequence of values iteratively. It suspends the function's execution temporarily, allowing it to yield a value back to the caller while retaining its state. This facilitates the generation of large sequences of values efficiently without storing them all in memory simultaneously.
- `\r` (carriage return) in `print`. Example: `print(f"\rpatata {i}", end='')`. When printed, it moves the cursor back to the beginning of the current line, allowing subsequent output to overwrite the existing content on that line. It's commonly used to create dynamic or updating text, like progress bars or status indicators. Is used in combination with end='' to ensure that the cursor moves back to the beginning of the line without starting a new line.


### Ex09
Create a package:
- `python3 -m build`
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

Install local package:
- `pip install ./dist/ft_package-0.0.1.tar.gz`
- `pip install ./dist/ft_package-0.0.1-py3-none-any.whl`

See package info:
- `pip show -v ft_package`
