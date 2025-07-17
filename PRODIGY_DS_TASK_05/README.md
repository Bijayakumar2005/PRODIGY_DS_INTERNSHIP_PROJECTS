# UK Traffic Accident Analysis

## 📌 Project Overview
This Python script analyzes UK traffic accident data to identify patterns related to:
- Temporal factors (hour, day, month)
- Weather conditions
- Road surface conditions
- Accident severity
- Geographic hotspots

## 📂 Dataset Requirements
- **File Name**: `Accident_Information.csv`
- **Expected Columns**:
  - Date/Time (as 'Date' or 'Accident_Date')
  - Location data ('Latitude', 'Longitude')
  - 'Weather_Conditions'
  - 'Road_Surface_Conditions'
  - 'Accident_Severity'

## 🛠️ Installation
1. Ensure Python 3.8+ is installed
2. Install required packages:
```bash
pip install pandas matplotlib seaborn folium
🚀 How to Run
Place your CSV file in the project directory

Execute the script:

bash
python accident_analysis.py
or specify the file path:

bash
python accident_analysis.py "path/to/your/file.csv"
📊 Outputs
The script will generate:

Console Output:

Dataset statistics

Column information

Analysis summaries

Visualizations (displayed interactively):

Temporal patterns (hourly/daily/monthly)

Weather impact analysis

Road condition analysis

Severity distribution

Interactive Map (opens in browser):

Heatmap of accident hotspots

Zoomable UK map with accident density

🧩 Code Structure
Key functions:

analyze_uk_accidents(filepath) - Main analysis function

Temporal analysis visualizations

Weather/Road condition analysis

Hotspot mapping with Folium

💡 Customization Options
Change file path:

python
analyze_uk_accidents("your/custom/path.csv")
Modify analysis focus by commenting/uncommenting sections

Adjust visualization styles in the set_palette and style.use calls

🐛 Troubleshooting
Common issues:

File not found: Verify correct path to CSV

Missing columns: Check your dataset contains required columns

Display issues: Ensure matplotlib backend is properly configured

📜 License
This project is open-source under the MIT License.