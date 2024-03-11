import sys


def is_punctuation(char):
    """
    Checks if the given character is a punctuation mark.

    Parameters:
        char (str): The character to check.

    Returns:
        bool: True if the character is a punctuation mark, False otherwise.
    """

    return char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def count_characters(text):
    """
    Counts the amount of different types of characters(upper, lower,
    punctuation, spaces, digits) in the given text and print them.

    Parameters:
        text (str): The input text to count characters from.

    Returns:
        None
    """

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:

        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif is_punctuation(char):
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    total_characters = len(text)

    print(f"The text contains {total_characters} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Main function of the program.
    It checks if the user has provided a text to count characters as
    an argument, and if not, it asks for it. Then it calls the
    count_characters function with the given text.

    Parameters:
        None

    Returns:
        None
    """

    s_text = ""

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) < 2 or sys.argv[1] is None:
            s_text = input("What is the text to count?\n")
            s_text += "\n"

        else:
            s_text = sys.argv[1]

        count_characters(s_text)

    except AssertionError as e:
        print("AssertionError:", e)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
