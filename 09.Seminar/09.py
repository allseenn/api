import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
import numpy as np


movie = pd.read_csv("movie.csv", encoding="UTF-8", engine="python", on_bad_lines="warn")
movie.head()

labeled_reviews, unlabeled_reviews = train_test_split(movie, train_size=0.2, random_state=56)

def train_model(labeled_data):
    vect =  TfidfVectorizer()
    x = vect.fit_transform(labeled_data["text"])
    y = labeled_data["label"]
    model = LogisticRegression()
    model.fit(x, y)
    return model, vect


model, vect = train_model(labeled_reviews) 

x_unlabeled = vect.transform(unlabeled_reviews["text"])

y_unlabeled_proba = model.predict_proba(x_unlabeled) 
uncertainties = -(y_unlabeled_proba * np.log2(y_unlabeled_proba)).sum(axis=1)

labeled_reviews_new = unlabeled_reviews.iloc[uncertainties.argsort()[:100]]
unlabeled_reviews_new = unlabeled_reviews.iloc[uncertainties.argsort()[-100:]] 

labeled_marks = pd.concat([labeled_reviews, labeled_reviews_new])
unlabeled_marks = pd.concat([unlabeled_reviews, unlabeled_reviews_new])

model, vectorized = train_model(labeled_marks) 


x_test = vect.transform(unlabeled_marks["text"]) 
y_test_predicted = model.predict(x_test) 

f1 = f1_score(unlabeled_marks["label"], y_test_predicted)



