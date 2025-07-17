import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load the dataset
data = pd.read_csv('PRODIGY_DS_INTERNSHIP_PROJECTS/PRODIGY_DS_TASK_04/twitter_validation.csv', header=None, 
                   names=['ID', 'Brand', 'Sentiment', 'Text'])

# Data cleaning
data = data.dropna()  # Remove any empty rows
data = data[data['Sentiment'] != 'Irrelevant']  # Filter out irrelevant entries

# 1. Overall Sentiment Analysis
sentiment_counts = data['Sentiment'].value_counts(normalize=True) * 100

# 2. Brand Analysis
brand_counts = data['Brand'].value_counts().head(10)
brand_sentiments = data.groupby(['Brand', 'Sentiment']).size().unstack().fillna(0)
top_brands = brand_sentiments.sum(axis=1).sort_values(ascending=False).head(5).index
brand_sentiments = brand_sentiments.loc[top_brands]

# 3. Text Analysis
from wordcloud import WordCloud

def generate_wordcloud(sentiment):
    text = ' '.join(data[data['Sentiment'] == sentiment]['Text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Visualization
plt.figure(figsize=(15, 15))

# 1. Overall Sentiment Pie Chart
plt.subplot(2, 2, 1)
plt.pie(sentiment_counts, labels=sentiment_counts.index, 
        autopct='%1.1f%%', colors=['green', 'red', 'blue'])
plt.title('Overall Sentiment Distribution')

# 2. Top Brands Bar Plot
plt.subplot(2, 2, 2)
brand_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Discussed Brands')
plt.xticks(rotation=45)

# 3. Brand Sentiment Heatmap
plt.subplot(2, 2, 3)
sns.heatmap(brand_sentiments, annot=True, fmt='g', cmap='YlGnBu')
plt.title('Sentiment Distribution by Top Brands')
plt.xlabel('Sentiment')
plt.ylabel('Brand')

# 4. Word Clouds for Each Sentiment
plt.subplot(2, 2, 4)
wordcloud = generate_wordcloud('Positive')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Sentiment Word Cloud')

plt.tight_layout()
plt.show()

# Additional Analysis
print("\n=== Detailed Analysis ===")
print(f"\n1. Overall Sentiment Distribution:\n{sentiment_counts}")
print(f"\n2. Top 5 Brands by Mention:\n{brand_counts.head(5)}")

# Sentiment by Brand
for brand in top_brands:
    brand_data = data[data['Brand'] == brand]
    sentiment_dist = brand_data['Sentiment'].value_counts(normalize=True) * 100
    print(f"\n3. Sentiment for {brand}:\n{sentiment_dist}")

# Most Common Words
from sklearn.feature_extraction.text import CountVectorizer

def get_top_words(sentiment, n=10):
    texts = data[data['Sentiment'] == sentiment]['Text']
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    word_counts = zip(vectorizer.get_feature_names_out(), X.sum(axis=0).tolist()[0])
    return sorted(word_counts, key=lambda x: x[1], reverse=True)[:n]

print("\n4. Most Common Words by Sentiment:")
for sentiment in ['Positive', 'Negative', 'Neutral']:
    print(f"\n{sentiment} words:")
    print(get_top_words(sentiment))


print("\nAnalysis complete.")