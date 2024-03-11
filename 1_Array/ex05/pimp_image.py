from PIL import Image
import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.

    It subtracts the input array from 255.

    Parameters:
        array (np.ndarray): The image to invert.

    Returns:
        np.ndarray: The inverted image.
    """

    try:
        inverted_array = np.subtract(255, array)

        Image.fromarray(inverted_array).show()

        return inverted_array

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_red(array) -> np.ndarray:
    """
    Returns an array with only the red channel values of the input array.

    It gets the red channel and stacks it with two arrays of zeros.

    Parameters:
        array (np.ndarray): The input array.

    Returns:
        np.ndarray: The red channel of the image.
    """

    try:
        red_array = array[:, :, 0]
        np_red = np.stack([red_array,
                           np.zeros_like(red_array),
                           np.zeros_like(red_array)], axis=2)

        Image.fromarray(np_red).show()

        return np_red

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_green(array) -> np.ndarray:
    """
    Returns an array with only the green channel values of the input array.

    It gets the green channel and stacks it with two arrays of zeros.

    Parameters:
        array (np.ndarray): The input array.

    Returns:
        np.ndarray: The green channel of the image.
    """

    try:
        green_array = array[:, :, 1]
        np_green = np.stack([np.zeros_like(green_array),
                            green_array,
                            np.zeros_like(green_array)],
                            axis=2)

        Image.fromarray(np_green).show()

        return np_green

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_blue(array) -> np.ndarray:
    """
    Returns an array with only the blue channel values of the input array.

    It gets the blue channel and stacks it with two arrays of zeros.

    Parameters:
        array (np.ndarray): The input array.

    Returns:
        np.ndarray: The blue channel of the image.
    """

    try:
        blue_array = array[:, :, 2]
        np_blue = np.stack([np.zeros_like(blue_array),
                            np.zeros_like(blue_array),
                            blue_array], axis=2)

        Image.fromarray(np_blue).show()

        return np_blue

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_grey(array) -> np.ndarray:
    """
    Returns an array with the grayscale of the input array.

    It gets the mean of the three channels and squeezes the array
    to remove the third dimension.

    Parameters:
        array (np.ndarray): The input array.

    Returns:
        np.ndarray: The grayscale array of the image.
    """

    try:
        grey_array = np.mean(array, axis=2, keepdims=True)

        np_grey = np.squeeze(grey_array, axis=2)

        Image.fromarray(np_grey).show()

        return np_grey

    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass
