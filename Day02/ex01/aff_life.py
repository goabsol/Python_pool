from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot the life expectancy over time for France as a line chart."""
    data = load("life_expectancy_years.csv")

    plt.figure(figsize=(10, 6))
    print(data.columns[1:])
    row = data.loc[data["country"] == "France"].values[0][1:]
    plt.plot(data.columns[1:], row, label="France")
    plt.title('Life Expectancy Over Time')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (years)')
    plt.xticks(ticks=range(0, len(data.columns[1:]), 40),
               labels=data.columns[1::40])
    if plt.get_backend().lower() == "agg":
        out = "life_expectancy_france.png"
        plt.savefig(out, bbox_inches="tight")
        print(f"Saved plot to {out}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
