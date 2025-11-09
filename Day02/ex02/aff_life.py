from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    if pop_str == "B":
        return float(pop_str[:-1]) * 1e9
    elif pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """Plot the population over time for Belgium and France."""
    data = load("population_total.csv")

    c1 = "Belgium"
    c2 = "France"

    c1_data = data[data['country'] == c1].iloc[:, 1:]
    c2_data = data[data['country'] == c2].iloc[:, 1:]

    c1_pop = c1_data.values.flatten()
    c2_pop = c2_data.values.flatten()
    years = c1_data.columns.astype(int)

    c1_pop = [preprocess_population(pop) for pop in c1_pop]
    c2_pop = [preprocess_population(pop) for pop in c2_pop]

    plt.plot(years, c1_pop, label=c1)
    plt.plot(years, c2_pop, label=c2)

    plt.title("Population in {} and {}".format(c1, c2))
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    max_pop = max(max(c1_pop), max(c2_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


if __name__ == "__main__":
    main()
