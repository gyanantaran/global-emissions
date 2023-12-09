import pandas as pd
from pandas import DataFrame

from src.utils.data_loader import emissions_df

# Define corresponding income categories
income_categories = ['Low-income', 'Lower-middle-income', 'Upper-middle-income', 'High-income']


def add_gdp_category_column(df: DataFrame) -> DataFrame:
    # Define income thresholds for categorization
    income_thresholds = [
        float('-inf'),
        1045,  # Low-income
        4095,  # Lower-middle-income
        12695,  # Upper-middle-income
        float('inf')
    ]

    # Calculate GDP per capita
    df['GDP_Per_Capita'] = df['Country.GDP'] / df['Country.Population']

    # Categorize based on GDP per capita
    df['GDP_Category'] = pd.cut(df['GDP_Per_Capita'], bins=income_thresholds, labels=income_categories, right=False)

    # Drop the intermediate column 'GDP_Per_Capita' if not needed
    df.drop('GDP_Per_Capita', axis=1, inplace=True)

    return df


emissions_df = add_gdp_category_column(emissions_df)

# Call the function to add the new column
if __name__ == "__main__":
    print(emissions_df['GDP_Category'])
