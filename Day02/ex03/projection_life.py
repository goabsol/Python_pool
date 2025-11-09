from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot the life expectancy against income per person for the year 1900."""
    path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_data = load(path)
    life_expectancy_data = load("life_expectancy_years.csv")
    year = "1900"
    income = income_data[year]
    life_expectancy = life_expectancy_data[year]

    plt.figure(figsize=(10, 6))
    plt.scatter(income, life_expectancy)
    plt.title("Life expectancy vs Gross domestic product (Year {})"
              .format(year))
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy (Years)")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
