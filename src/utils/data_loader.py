from src.utils.paths import data_loc, yearwise_loc

import pandas as pd

emissions_df = pd.read_csv(data_loc)
yearwise_df = pd.read_csv(yearwise_loc)
