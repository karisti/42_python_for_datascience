

def mean(values: list, len_vals: int) -> float:
    """
    Calculates the mean of the values in the list and returns it.

    Parameters:
        - values (list): A list of numbers.
        - len_vals (int): The length of the list.

    Returns:
        float: The mean of the values in the list.
    """

    mean = sum(values) / len_vals

    return float(mean)


def median(values: list, len_vals: int) -> float:
    """
    Calculates the median of the values in the list and returns it.

    Parameters:
        - values (list): A sorted list of numbers.
        - len_vals (int): The length of the list.

    Returns:
        float: The median of the values in the list.
    """

    median_idx = len_vals // 2

    if len_vals % 2 == 0:
        median = (values[median_idx - 1] +
                  values[median_idx]) / 2
    else:
        median = values[median_idx]

    return float(median)


def quartile(values: list, len_vals: int) -> float:
    """
    Calculates the first and third quartiles of the values
    in the list and returns them.

    Parameters:
        - values (list): A sorted list of numbers.
        - len_vals (int): The length of the list.

    Returns:
        float: The first and third quartiles of the values in the list.
    """

    q1_index = len_vals // 4
    q3_index = len_vals * 3 // 4

    if len_vals % 4 == 0:
        q1 = (values[q1_index - 1] + values[q1_index]) / 2
        q3 = (values[q3_index - 1] + values[q3_index]) / 2
    else:
        q1 = values[q1_index]
        q3 = values[q3_index]

    return [float(q1), float(q3)]


def var(values: list, len_vals: int) -> float:
    """
    Calculates the variance of the values in the list and returns it.

    Parameters:
        - values (list): A sorted list of numbers.
        - len_vals (int): The length of the list.

    Returns:
        float: The variance of the values in the list.
    """

    mean_val = mean(values, len_vals)
    var_sum = sum((value - mean_val) ** 2 for value in values)
    var = var_sum / len_vals

    return float(var)


def std(values: list, len_vals: int) -> float:
    """
    Calculates the standard deviation of the values in the list
    and stores it in the dictionary d_results

    Parameters:
        - values (list): A sorted list of numbers.
        - len_vals (int): The length of the list.

    Returns:
        float: The standard deviation of the values in the list.
    """

    std = var(values, len_vals) ** 0.5

    return float(std)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Prints the results of the calculations.

    Args:
        *args: Variable length argument list of values.
        **kwargs: Arbitrary keyword arguments representing
        the operations to be performed.

    Returns:
        None
    """

    operations = kwargs.values()
    vals = args

    vals_len = len(vals)
    vals_sorted = sorted(list(vals))

    for operation in operations:

        try:
            assert vals_len > 0, "ERROR"
            assert all(isinstance(val, (int, float)) for val in vals), \
                "ERROR"

            if operation == "mean":
                print(f"mean : {mean(vals, vals_len)}")

            elif operation == "median":
                print(f"median : {median(vals_sorted, vals_len)}")

            elif operation == "quartile":
                print(f"quartile : {quartile(vals_sorted, vals_len)}")

            elif operation == "var":
                print(f"var : {var(vals_sorted, vals_len)}")

            elif operation == "std":
                print(f"std : {std(vals_sorted, vals_len)}")

        except AssertionError as e:
            print(e)
        except Exception as e:
            print("Exception:", e)
