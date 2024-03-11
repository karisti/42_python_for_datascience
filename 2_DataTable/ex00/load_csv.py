import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the CSV data,
        or None if an error occurred.
    """

    try:

        assert isinstance(path, str), "The path must be a string"
        assert path.endswith(".csv"), "The file has not .csv extension"

        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)

        return data

    except AssertionError as e:
        print("AssertionError:", e)
        return None
    except Exception as e:
        print("Exception:", e)
        return None
