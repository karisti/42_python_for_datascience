import matplotlib.pyplot as plt
from load_csv import load


def display_country_life_expectancy(country: str, data) -> None:
    """
    Display the life expectancy of a country over the years.

    Parameters
        country(str): The country to display the life expectancy for.
        data(pd.DataFrame): The data to display the life expectancy from.

    Returns
        None

    Raises
        AssertionError: If the country does not exist in the dataset.
        AssertionError: If there is not enough data to display the life
        expectancy of the country.
    """

    assert country in data["country"].values, \
        f"The country '{country}' does not exist in the dataset"

    country_data = data[data["country"] == country]

    assert len(country_data.values) > 0 and \
        len(country_data.values[0]) > 1 and \
        len(country_data.columns) > 1, \
        f"Not enough data to display the life expectancy of '{country}'"

    years = country_data.columns[1:]
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.title(country + " Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(years[::40])
    plt.show()


def main():
    """
    Main function to display the life expectancy of a country.

    Parameters
        None

    Returns
        None
    """

    try:

        data = load("life_expectancy_years.csv")

        display_country_life_expectancy("Spain", data)

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
