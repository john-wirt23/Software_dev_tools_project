import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords as nltk_stopwords
import nltk

# Download stopwords
nltk.download('stopwords')

# Read the data
df_train = pd.read_csv('/home/john/Downloads/moved_imdb_reviews_small_lemm_train.tsv', sep='\t')
df_test = pd.read_csv('/home/john/Downloads/moved_imdb_reviews_small_lemm_test.tsv', sep='\t')

corpus_train = df_train['review_lemm']
corpus_test = df_test['review_lemm']
target_train = df_train['pos']

# Setting stop words variable using nltk_stopwords.words with language set to English
stop_words = list(nltk_stopwords.words('english'))

# Initializing TfidfVectorizer with stop_words variable for stopwords parameter
count_tf_idf = TfidfVectorizer(stop_words=stop_words)

# Fitting the training data and transforming both training and test data
tf_idf_train = count_tf_idf.fit_transform(corpus_train)
tf_idf_test = count_tf_idf.transform(corpus_test)

# Initializing and training the Logistic Regression model
model = LogisticRegression(max_iter=200, random_state=42)
model.fit(tf_idf_train, target_train)

# Make predictions on the training data for evaluation
train_predictions = model.predict(tf_idf_train)

# Calculate and print the accuracy on the training data
train_accuracy = accuracy_score(target_train, train_predictions)
print(f"Training Accuracy: {train_accuracy}")

# Make predictions on the test data
test_predictions = model.predict(tf_idf_test)

# Add predictions to the test data
df_test['pos'] = test_predictions

# Save the predictions to a CSV file without specifying the file extension
df_test.to_csv('predictions', index=False)

print("Predictions saved to 'predictions' file.")
