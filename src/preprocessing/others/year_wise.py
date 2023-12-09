import pandas as pd

from src.utils.data_loader import emissions_df
from src.utils.paths import yearwise_loc


def drop_non_numerical(df):
    # Select numerical columns except 'YEAR'
    numerical_cols = df.select_dtypes(include=['number']).columns
    non_numerical_cols = [col for col in df.columns if col not in numerical_cols and col != 'Year']

    # Drop non-numerical columns
    df_numeric = df.drop(columns=non_numerical_cols)

    return df_numeric


yearwise_df = drop_non_numerical(emissions_df).groupby('Year').sum().round(3)
yearwise_df.to_csv(yearwise_loc)