from src.utils.data_loader import emissions_df

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def basic_descriptive_statistics(df):
    """Calculate basic descriptive statistics for numerical columns."""
    numeric_columns = df.select_dtypes(include='number')
    summary_stats = numeric_columns.describe()
    missing_values = numeric_columns.isnull().sum()
    return summary_stats, missing_values


def yearly_trends(df):
    """Calculate average values for each numeric variable over the years."""
    numeric_columns = df.select_dtypes(include='number')
    return numeric_columns.groupby('Year').mean()


def top_bottom_countries(df, column, top_n=5):
    """Identify top and bottom countries based on a specific column."""
    top_countries = df.groupby('Country.Name')[column].mean().nlargest(top_n)
    bottom_countries = df.groupby('Country.Name')[column].mean().nsmallest(top_n)
    return top_countries, bottom_countries


def emissions_breakdown(df, columns):
    """Calculate the average contribution of each emission source."""
    return df[columns].mean()


def plot_boxplots(df, columns):
    """Create box plots for numerical variables."""
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='variable', y='value', data=pd.melt(df[columns]))
    plt.title('Boxplot of Selected Variables')
    plt.show()


def plot_histograms(df, columns):
    """Plot histograms for numerical variables."""
    df[columns].hist(bins=20, figsize=(12, 6))
    plt.suptitle('Histograms of Selected Variables')
    plt.show()


# Perform descriptive statistics analysis
summary_stats, missing_values = basic_descriptive_statistics(emissions_df)
# yearly_trends_data = yearly_trends(emissions_df)
# top_countries_mean_global_share_emissions, _ = top_bottom_countries(emissions_df, 'Emissions.Global Share.CO2.Total', top_n=10)
top_countries_mean_production_emissions, _ = top_bottom_countries(emissions_df, 'Emissions.Production.CO2.Total', top_n=10)
# top_countries_gdp, _ = top_bottom_countries(emissions_df, 'Country.GDP')
# emissions_data = emissions_breakdown(emissions_df, ['Emissions.Production.CH4', 'Emissions.Production.N2O',
#                                                     'Emissions.Production.CO2.Cement', 'Emissions.Production.CO2.Coal',
#                                                     'Emissions.Production.CO2.Gas', 'Emissions.Production.CO2.Oil',
#                                                     'Emissions.Production.CO2.Flaring',
#                                                     'Emissions.Production.CO2.Other'])


def main():
    # Visualizations
    plot_boxplots(emissions_df, ['Country.GDP', 'Country.Population'])
    plot_histograms(emissions_df, ['Country.GDP', 'Country.Population'])

    # Print or use the results as needed
    print("Summary Statistics:\n", summary_stats)
    # print("\nMissing Values:\n", missing_values)
    # print("\nYearly Trends:\n", yearly_trends_data)
    # print("\nTop Countries based on GDP:\n", top_countries_gdp)
    # print("\nTop Countries based on Mean Global Emission shares emission:\n", top_countries_mean_global_share_emissions)
    print("\nTop Countries based on Mean Production emission:\n", top_countries_mean_production_emissions)
    # print("\nEmissions Breakdown:\n", emissions_data)


if __name__ == "__main__":
    main()
