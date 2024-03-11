import sys


def check_odd_even(number: int):

    assert isinstance(number, int), "argument is not an integer"

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) == 2:
        i_arg = int(sys.argv[1])
        check_odd_even(i_arg)

except AssertionError as e:
    print("AssertionError:", e)
except ValueError:
    print("AssertionError: argument is not an integer")
