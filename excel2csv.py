import pandas as pd
import datetime

# Data from https://porssisahko.net/tilastot
xlsl_filename = "sahkon-hinta-010121-180125.xlsx"
dfs = pd.read_excel(xlsl_filename, sheet_name=None)
xlsldf = dfs["sahkon-hinnat"]

# Extract values from the df
datetimes = xlsldf.iloc[3:,0].values
costs = xlsldf.iloc[3:,1].values

# Make into a new df and save as csv
df = pd.DataFrame({"timestamp":datetimes, "cost":costs})
df.to_csv("data.csv", index=False)