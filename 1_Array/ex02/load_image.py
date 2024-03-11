import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file, print its shape and return it as a numpy array.

    Parameters:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image as a numpy array.
    """

    try:
        assert isinstance(path, str) and len(path) > 0, \
            "The path must be a string."

        img = Image.open(path)

        assert img is not None, "The image could not be loaded."
        assert img.format in ["JPEG", "JPG"], \
            "The image format is not supported."

        img_array = np.array(img)

        print("The shape of image is:", img_array.shape)

        return img_array

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
