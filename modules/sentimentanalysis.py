# -*- coding: utf-8 -*-
"""SentimentAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1re-dh3zI9x5LOvF0fRjezKZMhOBSlVFf
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_compound_sentiment_scores(list_of_news):
    # Initialize VADER so we can use it later
    sentimentAnalyser = SentimentIntensityAnalyzer()
    
    compound_sentiment_scores=[]
    for el in list_of_news:
        compound_sentiment_scores.append(sentimentAnalyser.polarity_scores(el)["compound"])
    
    return compound_sentiment_scores