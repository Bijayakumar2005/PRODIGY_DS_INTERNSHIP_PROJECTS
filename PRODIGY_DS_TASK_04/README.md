# Social Media Sentiment Analysis



## Overview
This project analyzes sentiment patterns in social media data to understand public opinion and attitudes toward various brands and topics. The analysis focuses on Twitter data categorized by brand/topic and sentiment (Positive, Negative, Neutral, or Irrelevant).

## Features

- **Sentiment Distribution Analysis**: Breakdown of overall sentiment percentages
- **Brand-Specific Insights**: Sentiment analysis for top mentioned brands
- **Text Analysis**: Word frequency and word cloud generation
- **Visualizations**: 
  - Pie charts
  - Bar plots
  - Heatmaps
  - Word clouds

## Dataset
The dataset (`twitter_validation.csv`) contains Twitter data with the following columns:
- `ID`: Unique identifier for each tweet
- `Brand`: The brand or topic being discussed
- `Sentiment`: Categorical sentiment (Positive, Negative, Neutral, Irrelevant)
- `Text`: The actual tweet content

## Requirements

- Python 3.6+
- Required packages:
  ```bash
  pandas
  matplotlib
  seaborn
  wordcloud
  scikit-learn
Installation



cd sentiment-analysis
Install dependencies:

bash
pip install -r requirements.txt
Usage
Place your twitter_validation.csv file in the project directory

Run the analysis script:

bash
python sentiment_analysis.py
View results:

Visualizations will be displayed and saved as sentiment_analysis_results.png

Text analysis results will be printed to the console

Output
The analysis generates:

Visualizations:

Overall sentiment distribution (pie chart)

Top mentioned brands (bar chart)

Brand sentiment heatmap

Word clouds for each sentiment type

Text Analysis:

Most common words by sentiment category

Sentiment distribution by top brands

Example Results
Overall Sentiment Distribution
Sentiment	Percentage
Positive	28.3%
Negative	32.1%
Neutral	30.7%
Irrelevant	8.9%
Top 5 Brands by Mention Count
Call of Duty

FIFA

Grand Theft Auto

Rainbow Six

NBA 2K

Customization
To analyze different datasets:

Modify the column names in the script to match your CSV file

Adjust visualization parameters in the plotting functions

Change the number of top brands displayed by modifying the head() parameter

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Contact
For questions or suggestions, please contact: bijayakumarrout2005@gmail.com