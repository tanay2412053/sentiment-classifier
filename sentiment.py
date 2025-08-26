from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

X_train = ["Amazing movie", "Terrible film", "Not bad", "Absolutely loved it", "Worst ever"]
y_train = ["positive", "negative", "neutral", "positive", "negative"]

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

clf = LogisticRegression()
clf.fit(X_train_vec, y_train)

movie_name = input("Enter movie name: ")
review = input(f"Enter your review for '{movie_name}': ")

X_test_vec = vectorizer.transform([review])
pred = clf.predict(X_test_vec)[0]
prob = np.max(clf.predict_proba(X_test_vec))

print(f"Movie: {movie_name}")
print(f"Predicted Sentiment: {pred} with score {prob:.2f}")
