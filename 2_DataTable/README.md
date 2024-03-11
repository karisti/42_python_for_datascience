## 2. DataTable

### Ex00
Pandas usage.
- `pd.read_csv(path)` loads csv from given path.


### Ex01
pandas to manage data, matplotlib to display graphs.

Pandas:
- [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
- [Selecting rows from Pandas DataFrame](https://appdividend.com/2022/06/17/pandas-select-rows/)
- `country_data = data[data["country"] == country]` select rows from a DataFrame using a boolean vector the same length as the DataFrame’s index. Its possible to use operators like `>`, `<`, etc.
- `country_data.columns` gets list of all columns.
- `country_data.values` gets list of all values.

Matplot:
- [Matplot](https://www.activestate.com/resources/quick-reads/how-to-display-a-plot-in-python/)
- `plt.plot(columns, values)` sets points.
- `plt.title("")` sets graph title.
- `plt.xlabel("")` sets x axe label. Same with `ylabel`.
- `plt.xticks(years[::40], ["tag1", "tag2"])` sets ticks from list. Its possible to give a second list with the tags to show. Same with `yticks`.
- `plt.show()` shows graph.

Other graph libraries: [Plotly express](https://plotly.com/python/plotly-express/)


### Ex02
Similar to ex01 with two plots and legend.
- Data needs to be normalized, as matplot does not understand 10B, 2M, 1k format.
- `plt.legend(list(arg), loc="lower right")` puts a legend.


### Ex03
Similar with scatter graph.
- `plt.scatter(year_income_per_person, year_life_expectancy)` creates scatter.
- `plt.xscale('log')` puts logarithmic scale.
