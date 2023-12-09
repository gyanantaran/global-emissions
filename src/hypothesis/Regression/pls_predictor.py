# this model aims to make a model that predicts the `Y` factor in
# 'next' year from given values of `Y`'s in the previous k-years

from src.utils.data_loader import yearwise_df

years = yearwise_df['Year'].to_list()
co2_emission = yearwise_df['Emissions.Production.CO2.Total'].to_list()

# Making X and Y
X = []
Y = []
k_last_years = 3
for i in range(k_last_years, len(years)):
    cur_year = years[i]
    X.append(years[i-k_last_years:i])
    Y.append(co2_emission[i])

print(len(X))
print(len(Y))
