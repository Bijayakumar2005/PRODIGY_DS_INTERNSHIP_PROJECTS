# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_text

# Load the dataset
data = pd.read_csv('PRODIGY_DS_INTERNSHIP_PROJECTS/PRODIGY_DS_TASK_03/bank.csv', delimiter=';')

# Data preprocessing
# Convert categorical variables to numeric using Label Encoding
label_encoders = {}
categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Target variable encoding
data['y'] = data['y'].map({'no': 0, 'yes': 1})

# Split into features and target
X = data.drop('y', axis=1)
y = data['y']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the decision tree classifier
dt_classifier = DecisionTreeClassifier(
    max_depth=5,  # Limiting depth to prevent overfitting
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)
dt_classifier.fit(X_train, y_train)

# Make predictions
y_pred = dt_classifier.predict(X_test)

# Evaluate the model
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Display feature importances
print("\nFeature Importances:")
for feature, importance in zip(X.columns, dt_classifier.feature_importances_):
    print(f"{feature}: {importance:.4f}")

# Optionally print tree structure (for small trees)
print("\nDecision Tree Structure:")
tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
print(tree_rules[:1000])  # Print first 1000 characters to avoid huge output