import matplotlib.pyplot as plt
from load_csv import load


def get_plot_color(idx: int) -> str:
    """
    Get the color for the plot.

    Parameters
        idx (int): Index of the plot

    Returns
        str: Color of the plot
    """

    colors = ["blue", "green", "red", "yellow", "black", "orange"]

    return colors[idx % len(colors)]


def population_str_to_float(s_population: str) -> float:
    """
    Convert a string population to a float.

    Parameters
        s_population (str): Population as a string

    Returns
        float: Population as a float
    """

    if s_population.endswith("k"):
        return float(s_population[:-1]) * 1000
    elif s_population.endswith("M"):
        return float(s_population[:-1]) * 1000000
    elif s_population.endswith("B"):
        return float(s_population[:-1]) * 1000000000
    else:
        return float(s_population)


def normalize_population(population: list) -> list:
    """
    Normalize the population to the same scale.

    Parameters
        population (list): Population values

    Returns
        list: Normalized float population values
    """

    return [population_str_to_float(p) for p in population]


def diplay_country_population(data, country: str,
                              color: str) -> None:
    """
    Display the population of a country.

    Parameters
        data (pd.DataFrame): Population data
        country (str): Country to display
        color (str): Color of the plot

    Returns
        None

    Raises
        AssertionError: If the country does not exist in the dataset
        AssertionError: If there is not enough data to display the population
    """

    assert country in data["country"].values, \
        f"The country '{country}' does not exist in the dataset"

    country_data = data[data["country"] == country]

    assert len(country_data.values) > 0 and \
        len(country_data.values[0]) > 1 and \
        len(country_data.columns) > 1, \
        f"Not enough data to display population of '{country}'"

    years = country_data.columns[1:-50]
    population = normalize_population(country_data.values[0][1:-50])
    plt.plot(years, population, label=country, color=color)


def display_countries_population(data, *arg) -> None:
    """
    Display the population of two countries.

    Parameters
        data (pd.DataFrame): Population data
        arg (list): List of countries to display the population

    Returns
        None

    Raises
        AssertionError: If there are not enough columns in the dataset
    """

    assert len(data.columns) > 1, \
        "Not enough columns"

    for idx, country in enumerate(arg):

        plot_color = get_plot_color(idx)

        diplay_country_population(data, country, plot_color)

    years = data.columns[1:-50:40]
    plt.xticks(years)
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.legend(list(arg), loc="lower right")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()


def main():
    """
    Main function to display the population of a country.

    Parameters
        None

    Returns
        None
    """

    try:

        data = load("population_total.csv")

        display_countries_population(data, "Spain", "France")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":

    main()
