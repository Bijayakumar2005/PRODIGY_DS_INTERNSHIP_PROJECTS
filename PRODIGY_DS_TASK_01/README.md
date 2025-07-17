
# Population Trends by Income Group (1960–2023)

This project analyzes global population trends grouped by World Bank income classifications using data from the World Bank dataset.

## 📊 Project Description

The script:
- Loads population data (1960–2023) for all countries.
- Merges it with country metadata including region and income group.
- Aggregates population totals by income group for each year.
- Visualizes the population trend over time for:
  - Low income
  - Lower middle income
  - Upper middle income
  - High income countries

## 📁 Files Required

Place the following files in the same directory as the Python script:

- `API_SP.POP.TOTL_DS2_en_csv_v2_127006.csv` – Main population dataset.
- `Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_127006.csv` – Metadata including income group.

## ▶️ How to Run

1. Install required libraries if not already installed:

```bash
pip install pandas matplotlib
```

2. Run the Python script:

```bash
python population_trend_by_income_group.py
```

3. The script will display a line chart showing population trends by income group from 1960 to 2023.

## 📌 Note

- Ensure that the CSV file paths are correctly set relative to your script.
- If you move the files, update the paths accordingly.

## 📷 Output

The output is a plot showing how the total population has changed over time for each income group.

## 📚 Data Source

- [World Bank Population Data](https://data.worldbank.org/indicator/SP.POP.TOTL)
