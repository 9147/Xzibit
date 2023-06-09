import joblib
from domain_model import check_domain
from auth_model import check_auth
import pickle
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

def check_news(domain,text):
    correct=0
    # text="Maharashtra chief minister Eknath Shinde has appealed to the masses to cooperate for the restoration of peace after violence in Kolhapur district on Tuesday. Normalcy returned late in the afternoon and evening as there was regular traffic, though vehicles were fewer, around Shivaji Chowk and the KMC main building nearby. Almost 90% of shops, trade and business establishments remained shut."
    correct += check_domain(domain)
    correct += check_auth(text)
    svm_model = joblib.load("svm_model.sav")


    # Load the TF-IDF vectorizer from the file
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf_vectorizer = pickle.load(f)

    tfidf_features = tfidf_vectorizer.transform([text])


    #   Make predictions using the SVM model
    prediction = svm_model.predict(tfidf_features)
    if prediction[0]=='real':
        correct+=1


    svm_model_sent= joblib.load("svm_model_sent.sav")
    sia = SentimentIntensityAnalyzer()
    test_2=np.array([sia.polarity_scores(text)['compound']])
    if svm_model_sent.predict(test_2.reshape(-1,1))=='real':
        correct+=1
    return correct*25


print(check_news("https://www.zeenews.india.com","Maharashtra chief minister Eknath Shinde has appealed to the masses to cooperate for the restoration of peace after violence in Kolhapur district on Tuesday. Normalcy returned late in the afternoon and evening as there was regular traffic, though vehicles were fewer, around Shivaji Chowk and the KMC main building nearby. Almost 90% of shops, trade and business establishments remained shut."))