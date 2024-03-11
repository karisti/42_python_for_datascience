import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def display_image_with_axes(img, cmap):
    """
    Display an image with axes using matplotlib.

    Parameters:
        img (np.ndarray): The image to display.
        cmap (str): The color map to use.

    Returns:
        None
    """

    plt.imshow(img, cmap=cmap)
    plt.show()


def zoom(img_array, x_start=100, x_end=500, y_start=450, y_end=850):
    """
    Zoom an image by slicing it and return the zoomed image.

    Parameters:
        img_array (np.ndarray): The image to zoom.
        x_start (int): The start of the x-axis slice. Default is 100.
        x_end (int): The end of the x-axis slice. Default is 500.
        y_start (int): The start of the y-axis slice. Default is 450.
        y_end (int): The end of the y-axis slice. Default is 850.

    Returns:
        np.ndarray: The zoomed image.
    """

    # Zoom the image by slicing it
    zoomed_img = img_array[x_start:x_end, y_start:y_end, 0:1]

    return zoomed_img


def transpose(img_array):
    """
    Rotates an image by transposing it. Returns the transposed image.
    The transpose of a matrix is a new matrix whose rows are the columns
    of the original.

    Parameters:
        img_array (np.ndarray): The image to transpose.

    Returns:
        np.ndarray: The transposed image.
    """

    rotated_img = []
    for x in range(img_array.shape[1]):  # iterate over the columns

        row = []
        for y in range(img_array.shape[0]):  # iterate over the rows
            row.append(img_array[y][x][0])
        rotated_img.append(row)

    return np.array(rotated_img)


def main():
    """
    Main function. Load an image, zoom it, transpose it and display it.

    Parameters:
        None

    Returns:
        None
    """

    try:
        # Load the image
        original_img = ft_load("animal.jpeg")

        # Zoom the image
        zoomed_img = zoom(original_img)
        print("The shape of image is:",
              zoomed_img.shape, "or", zoomed_img.shape[:2])
        print(zoomed_img)

        # Transpose the image
        transposed_img = transpose(zoomed_img)
        print("New shape after Transpose:",
              transposed_img.shape[:2])
        print(transposed_img)

        # Display transposed image
        display_image_with_axes(transposed_img, cmap="gray")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
