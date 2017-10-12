import nltk

"""
Helper functions for data mining lab session 2017 Fall

Notations:
d - document
D - documents
V - vowels
w - word
W - words
l - letter
"""

from collections import Counter
from copy import deepcopy
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import random

stopWords = stopwords.words('english')
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True) # Casual language tokenizer


def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

"""check_missing_values && add_dummy_data: Helpers for datasets"""
__author__      = "Elvis Saravia"
__modifier      = "Abner Tellez"
__copyright__   = "Copyright 2017, NTHU"

def check_missing_values(row): 
    return "The amoung of missing records is: ", Counter(row)[True] # Better way to count and check missing values, using Counter library

def add_dummy_data(dummy_data, n, random_missing_values = False) : 
    dummy_list = []
    for x in range(0, n):
        dummy_value = deepcopy(dummy_data)
        if (random_missing_values):
            dummy_value.pop(random.choice(list(dummy_data.keys())), None) 
        dummy_list.append(dummy_value)
    return dummy_list

"""
    Tokenize text using the nltk library
"""
def tokenize_text(text, remove_stopwords = False):
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in tknzr.tokenize(d):
            if (word not in stopWords or not remove_stopwords): # Filter stop words using parameter
                tokens.append(word)
    return tokens

def reduce_words(words, relevant_number = 5) :
    new_words = []
    for d in words:
        if (d[0] not in stopWords and d[1] >= relevant_number):
            new_words.append(d)
    return new_words



