## 1. Array

### Ex00
`zip()` function is used to combine multiple iterables (like lists, tuples, etc.) into tuples. It takes in two or more iterables and returns an iterator that produces tuples where the i-th tuple contains the i-th element from each of the input iterables. It stops with the shortest list.
```
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)

for item in zipped:
    print(item)
```


### Ex01
Numpy usage to load and manage data tables.
- Create numpy array (np.ndarray): `np.array([[1, 2], [3, 4]])`.
- Get numpy array shape: `np_array.shape`.
- Array dimensions: `len(np_array.shape)`.
- Slicing: We pass slice instead of index like this: `[start:end]` or `[start:end:step]`.
    - If we don't pass start its considered 0.
    - If we don't pass end its considered length of array in that dimension.
    - If we don't pass step its considered 1.
- Convert np array to python lists: `ndarray.tolist()`.
- `numpy.arange()` returns an array with evenly spaced values within a specified range. `np.arange(0, 10, 2)` outputs `[0 2 4 6 8]`.

Example:
```
np_array = np.array([[1, 2], [3, 4]])
print("NP Array:", np_array)
"""
NP Array:
[[1 2]
 [3 4]]

"""

np_shape = np_array.shape
print("Shape:", np_shape)
"""
Shape: (2, 2)
"""

np_dimension = len(np_array.shape)
print("Dimension:", np_dimension)
"""
Dimension: 2
"""

np_sliced_array = np_array[0:1]
print("Sliced Array:", np_sliced_array)
"""
Sliced Array: [[1 2]]
"""

list_array = np_sliced_array.tolist()
print("List Array:", list_array)
"""
List Array: [[1, 2]]
"""
```


### Ex02
[Pillow image](https://pillow.readthedocs.io/en/stable/reference/Image.html) usage to load and manage images.

- `Image.open(path)` loads image.
- `img.format` gets the loaded image format.


### Ex03
matplotlib usage to show graphics. See [graph examples](https://matplotlib.org/stable/gallery/index.html). Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias: `import matplotlib.pyplot as plt`.
- `plt.imshow(img)` puts the image. Example in grayscale: `plt.imshow(img, cmap="gray")`
- `plt.show()` to show window.
- `plt.xticks()` and `plt.yticks()` to customize the tick locations and labels.


### Ex04
Image rotation by transposing it. The transpose of a matrix is a new matrix whose rows are the columns of the original. It can be done iterating the matrix columns and rows or with `zip(*<matrix>)`.


### Ex05
More numpy and pillow.
- `Image.fromarray(inverted_array).show()` creates an image from numpy array and shows it.
- `np.subtract(255, array)` subtracts the input array from 255.
- `np.stack([np.zeros_like(blue_array), np.zeros_like(blue_array), blue_array], axis=2)` creates a new array by stacking three arrays, where the first two arrays are filled with zeros and the third array is the blue_array.
- `np.mean(array, axis=2, keepdims=True)` calculates the mean of array values of the axis 2. It keeps the original dims to avoid dimension errors.
- `np.squeeze(grey_array, axis=2)` removes single-dimensional entry from the shape of the grey_array along the specified axis.
