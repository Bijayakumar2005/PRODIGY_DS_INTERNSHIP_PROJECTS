# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots (updated style name)
plt.style.use('seaborn-v0_8')  # This works in newer matplotlib versions
sns.set_style("whitegrid")
sns.set_palette("Set2")

# Load the data
try:
    df = pd.read_csv('PRODIGY_DS_INTERNSHIP_PROJECTS/PRODIGY_DS_TASK_02/gender_submission.csv')
except FileNotFoundError:
    print("Error: File 'gender_submission.csv' not found in the current directory.")
    exit()

# =============================================
# 1. Basic Data Exploration
# =============================================
print("="*50)
print("1. BASIC DATA EXPLORATION")
print("="*50)

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Dataset information
print("\nDataset information:")
print(df.info())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# =============================================
# 2. Survival Analysis
# =============================================
print("\n" + "="*50)
print("2. SURVIVAL ANALYSIS")
print("="*50)

# Calculate survival statistics
total_passengers = len(df)
survivors = df['Survived'].sum()
non_survivors = total_passengers - survivors
survival_rate = survivors / total_passengers

print(f"\nTotal passengers: {total_passengers}")
print(f"Number of survivors: {survivors}")
print(f"Number of non-survivors: {non_survivors}")
print(f"Survival rate: {survival_rate:.2%}")

# =============================================
# 3. Data Visualization
# =============================================
print("\n" + "="*50)
print("3. DATA VISUALIZATION")
print("="*50)

# Create figure with subplots
plt.figure(figsize=(15, 10))

# 3.1 Survival distribution pie chart
plt.subplot(2, 2, 1)
df['Survived'].value_counts().plot.pie(autopct='%1.1f%%', 
                                      labels=['Did Not Survive', 'Survived'],
                                      colors=['#ff9999','#66b3ff'],
                                      explode=(0.1, 0),
                                      shadow=True)
plt.title('Survival Distribution', fontweight='bold')
plt.ylabel('')

# 3.2 Survival distribution bar plot
plt.subplot(2, 2, 2)
ax = sns.countplot(x='Survived', data=df)
plt.title('Survival Count', fontweight='bold')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')

# Add counts on top of bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 5), 
                textcoords='offset points')

# 3.3 Survival streaks analysis
plt.subplot(2, 2, 3)
df['streak'] = df['Survived'].ne(df['Survived'].shift()).cumsum()
streak_counts = df.groupby('streak').size()
survival_streaks = streak_counts[df.groupby('streak')['Survived'].first() == 1]
death_streaks = streak_counts[df.groupby('streak')['Survived'].first() == 0]

# Plot survival streaks
plt.bar(survival_streaks.index, survival_streaks.values, color='green', alpha=0.6, label='Survival Streaks')
plt.bar(death_streaks.index, death_streaks.values, color='red', alpha=0.6, label='Death Streaks')
plt.title('Survival and Death Streaks', fontweight='bold')
plt.xlabel('Streak ID')
plt.ylabel('Length of Streak')
plt.legend()

# 3.4 Cumulative survival
plt.subplot(2, 2, 4)
df['cumulative_survival'] = df['Survived'].cumsum()
plt.plot(df['PassengerId'], df['cumulative_survival'], color='blue', linewidth=2)
plt.title('Cumulative Number of Survivors', fontweight='bold')
plt.xlabel('Passenger ID')
plt.ylabel('Cumulative Survivors')
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

# =============================================
# 4. Advanced Analysis (with limited data)
# =============================================
print("\n" + "="*50)
print("4. ADVANCED ANALYSIS (WITH LIMITED DATA)")
print("="*50)

# Calculate longest streaks
print("\nLongest survival streaks:")
print(survival_streaks.nlargest(5))

print("\nLongest death streaks:")
print(death_streaks.nlargest(5))

# Calculate survival rate by passenger ID ranges
df['id_group'] = pd.cut(df['PassengerId'], bins=5)
group_survival = df.groupby('id_group')['Survived'].mean()

print("\nSurvival rate by passenger ID groups:")
print(group_survival)

# =============================================
# 5. What-If Analysis (if we had full dataset)
# =============================================
print("\n" + "="*50)
print("5. WHAT-IF ANALYSIS (IF WE HAD FULL DATASET)")
print("="*50)
print("\nWith the full Titanic dataset, we would typically analyze:")
print("- Survival by passenger class (Pclass)")
print("- Survival by gender (Sex)")
print("- Survival by age groups")
print("- Family size impact (SibSp + Parch)")
print("- Embarkation port effects")
print("- Cabin location patterns")
print("- Title extraction from names (Mr, Mrs, Miss, etc.)")