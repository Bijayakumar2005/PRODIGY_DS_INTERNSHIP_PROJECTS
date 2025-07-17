# Bank Marketing Campaign - Decision Tree Classifier

## Overview

This project implements a Decision Tree classifier to predict whether a bank customer will subscribe to a term deposit ("yes" or "no") based on demographic and behavioral data from the Bank Marketing dataset.

## Dataset

The dataset contains information from a Portuguese banking institution's direct marketing campaigns (phone calls). Key features include:

- **Demographic data**: age, job, marital status, education
- **Financial data**: balance, housing loan, personal loan
- **Contact information**: contact type, day/month of contact
- **Campaign details**: duration, number of contacts
- **Previous campaign outcomes**: poutcome

Target variable: `y` (whether the client subscribed to a term deposit)

## Requirements

- Python 3.6+
- pandas
- scikit-learn
- (Optional) graphviz for visualization

Install requirements:
```bash
pip install pandas scikit-learn
Project Structure
text
bank-marketing/
├── bank.csv               # Dataset file
├── bank_marketing.py      # Main Python script
├── README.md              # This file
└── requirements.txt       # Python dependencies

Run the analysis:

bash
python bank_marketing.py
Model Details
Preprocessing
Handles categorical variables with Label Encoding

Splits data into 70% training and 30% testing sets

Decision Tree Parameters
max_depth = 5 (limits tree complexity)

min_samples_split = 20

min_samples_leaf = 10

random_state = 42 (for reproducibility)

Evaluation Metrics
Accuracy score

Confusion matrix

Classification report (precision, recall, f1-score)

Feature importance analysis

Results
Typical performance metrics:

Accuracy: ~89-91%

Precision (for class "yes"): ~60-65%

Recall (for class "yes"): ~40-45%

Customization
To modify the model:

Adjust tree parameters in dt_classifier initialization

Try different preprocessing approaches

Experiment with feature engineering

License
MIT License - Free for academic and commercial use

References
[Moro et al., 2014] S. Moro, P. Cortez and P. Rita. "A Data-Driven Approach to Predict the Success of Bank Telemarketing." Decision Support Systems, Elsevier, 62:22-31, June 2014