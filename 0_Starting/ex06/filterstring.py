import sys
from ft_filter import ft_filter


def filter_string(text, word_length):
    """
    This function filters a string and returns a list of
    words with a length greater than a given number.

    Parameters:
        text (str): The string to filter.
        word_length (int): The minimum length of the words to return.

    Returns:
        list: A list of words with a length greater than word_length.
    """

    return list(ft_filter(lambda word: len(word) > word_length, text.split()))


def main():
    """
    Main function of the program. It checks if the user has
    provided a text and a number as arguments. Then it calls
    the filter_string function with the given text and number.

    Parameters:
        None

    Returns:
        None
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        s = sys.argv[1]
        n = int(sys.argv[2])

        assert isinstance(s, str), "the arguments are bad"
        assert isinstance(n, int), "the arguments are bad"

        print(filter_string(s, n))

    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
