

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    This function calculates the BMI (Body Mass Index) for a list of people
    given their height and weight. The BMI is calculated as the weight in
    kilograms divided by the square of the height in meters.

    Parameters:
        height: A list of integers or floats representing the height of each
        person in meters.
        weight: A list of integers or floats representing the weight of each
        person in kilograms.

    Returns:
        list: A list of integers or floats representing the BMI of each person.
    """

    try:
        # Input validation
        assert isinstance(height, list) and \
            isinstance(weight, list), \
            "Height and weight must be lists"
        assert len(height) == len(weight), \
            "Height and weight lists must be of the same length"

        bmi_values = []
        for h, w in zip(height, weight):

            # Input validation
            assert isinstance(h, (int, float)) and \
                isinstance(w, (int, float)), \
                "Height and weight must be integers or floats"
            assert h > 0 and w > 0, "Height and weight must be positive values"

            bmi = w / (h ** 2)
            bmi_values.append(bmi)

        return bmi_values

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function takes a list of BMI values and a limit, and returns a list
    of booleans indicating whether each BMI value is greater than the limit.

    Parameters:
        bmi: A list of integers or floats representing the BMI of each person.
        limit: An integer representing the limit to compare the BMI values to.

    Returns:
        list: A list of booleans indicating whether each BMI value is greater
        than the limit.
    """

    try:
        # Input validation
        assert isinstance(bmi, list), "BMI must be a list"
        assert isinstance(limit, int), \
            "Limit must be integer"

        limits = []
        for b in bmi:

            # Input validation
            assert isinstance(b, (int, float)), \
                "BMI values must be integers or floats"

            limits.append(b > limit)

        return limits

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
