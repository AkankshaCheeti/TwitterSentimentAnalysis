import json
import os
import pandas as pd
import json_lines
import nltk
from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize 
from collections import Counter
from nltk import FreqDist
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
import re;
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import matplotlib.pyplot as plt

# POS tagger dictionary
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
def token_stop_pos(text):
    tags = pos_tag(word_tokenize(text))
    newlist = []
    stop_words = set(stopwords.words('english'))
    for word, tag in tags:
        if word.lower() not in stop_words:
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist


wordnet_lemmatizer = WordNetLemmatizer()
def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# function to calculate vader sentiment
def vadersentimentanalysis(review):
    vs = analyzer.polarity_scores(review)
    return vs['compound']

# function to analyse
def vader_analysis(compound):
    if compound >= 0.5:
        return 1
    elif compound <= -0.5 :
        return -1
    else:
        return 0


def vader_sentiment(dataframe):
    dataframe['POS tagged'] = dataframe['text'].apply(token_stop_pos)
    # print(dataframe.head())

    dataframe['Lemma'] = dataframe['POS tagged'].apply(lemmatize)
    # print(dataframe.head())

    fin_data = pd.DataFrame(dataframe[['text', 'Lemma','date']])


    fin_data['Vader Sentiment'] = fin_data['Lemma'].apply(vadersentimentanalysis)
    fin_data['vader_sentiment'] = fin_data['Vader Sentiment'].apply(vader_analysis)
    #fin_data['vader_sentiment'] = ((fin_data['vader_sentiment'] + 1) / 2) * 0.5
    fin_data.head()
    start_date = pd.to_datetime('2021-01-01', utc=True)
    end_date = pd.to_datetime('2023-04-01', utc=True)
    # print(tb_counts)
    fin_data = fin_data[(pd.to_datetime(fin_data['date']) >= start_date) & (pd.to_datetime(fin_data['date']) <= end_date)]
    '''
    senti_counts = fin_data.groupby(['date', 'vader_sentiment'])['vader_sentiment'].count().unstack(fill_value=0)
    senti_counts.columns = ['Negative', 'Neutral', 'Positive']
    senti_counts.reset_index(inplace=True)
    senti_counts.to_csv('MSFTvadersentiment_scorescount.csv', index=False)
    '''
    # print(tb_counts)
    #fin_data = fin_data[(pd.to_datetime(fin_data['date']) >= start_date) & (pd.to_datetime(fin_data['date']) <= end_date)]
    df2 = fin_data.groupby('date')['vader_sentiment'].mean().reset_index()

    return df2