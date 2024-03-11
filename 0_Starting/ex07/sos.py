import sys


MORSE_CODES = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def encode_morse(text):
    """
    This function encodes a string to Morse code.

    Parameters:
        text (str): The string to encode.

    Returns:
        str: The Morse code of the given string.

    Raises:
        AssertionError: If the given argument is not a string.
        AssertionError: If the given string contains non-alphanumeric
        characters.
    """

    assert isinstance(text, str), "the arguments are bad"
    assert text.isalnum(), "the arguments are bad"

    return ' '.join(MORSE_CODES[char.upper()] for char in text)


def main():
    """
    Main function of the program. It checks if the user has
    provided a text to encode to Morse code as an argument.
    Then it calls the encode_morse function with the given text.

    Parameters:
        None

    Returns:
        None
    """

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        text = sys.argv[1]
        morse_text = encode_morse(text)
        print(morse_text)

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
