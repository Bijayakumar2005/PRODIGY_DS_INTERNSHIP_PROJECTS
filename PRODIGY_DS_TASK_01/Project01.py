
import pandas as pd
import matplotlib.pyplot as plt

# Load the main population data
population_df = pd.read_csv("Task-01/API_SP.POP.TOTL_DS2_en_csv_v2_127006.csv", skiprows=4)

# Load the metadata for countries (includes income group and region)
metadata_df = pd.read_csv("Task-01/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_127006.csv")

# Merge datasets on Country Code to include Income Group info
merged_df = pd.merge(
    population_df,
    metadata_df[["Country Code", "Region", "IncomeGroup"]],
    on="Country Code",
    how="left"
)

# Define the range of years to include in the analysis
years = [str(year) for year in range(1960, 2024)]

# Group by income group and sum population for each year
grouped = merged_df.groupby("IncomeGroup")[years].sum()

# Transpose for plotting (years as index)
grouped_T = grouped.T
grouped_T.index = grouped_T.index.astype(int)

# Plotting the population trends for each income group
plt.figure(figsize=(12, 7))
for income_group in grouped_T.columns:
    plt.plot(grouped_T.index, grouped_T[income_group], label=income_group)

plt.title("Population Trends by Income Group (1960–2023)")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.legend(title="Income Group")
plt.grid(True)
plt.tight_layout()
plt.show()
