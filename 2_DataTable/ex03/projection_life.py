import matplotlib.pyplot as plt
from load_csv import load


def display_graph(life_expectancy, income_per_person, year: str) -> None:
    """
    Display the projection of life expectancy in relation to the
    gross national product of the year 1900 for each country.

    Parameters
        life_expectancy (pd.DataFrame): Life expectancy data
        income_per_person (pd.DataFrame): Income per person data
        year (str): Year to display the graph
    """

    assert year in life_expectancy, \
        f"No data for year '{year}' in life expectancy"
    assert year in income_per_person, \
        f"No data for year '{year}' in income per person"

    year_life_expectancy = life_expectancy[year]
    year_income_per_person = income_per_person[year]

    plt.scatter(year_income_per_person, year_life_expectancy)
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title(year)
    plt.show()


def main():
    """
    Main function to display the projection of life expectancy in
    relation to the gross national product of the year 1900 for
    each country.

    Parameters
        None

    Returns
        None
    """

    try:
        life_expectancy = load("life_expectancy_years.csv")
        income_per_person = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

        display_graph(life_expectancy, income_per_person, year='1900')

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
