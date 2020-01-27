#!/usr/bin/python

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
import textdistance


def read_dictionary(path):
    file = open(path,'r')
    return file.read().lower().split('\n')

# Generate sentiment scores
def generate_score(text, list_to_compare):
    stemmer = PorterStemmer()
    numWords = 0
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(plural) for plural in tokens]
    for word in tokens:
        if word in list_to_compare:
            numWords  += 1
    
    cumsum = numWords
    return cumsum

# Relative score function
def relative_score(score, wordcount):
    return round(score / wordcount,4) if wordcount != 0 else 0

# Calculating polarity score
def polarity_score(positive_score, negative_score):
    pol_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    return pol_score

# Counting total words
def total_word_count(text):
    stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(plural) for plural in tokens]
    return len(tokens)

# Calculating Average sentence length 
def average_sentence_length(text):
    stemmer = PorterStemmer()
    sentence_list = sent_tokenize(text)
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(plural) for plural in tokens]
    average_sent_length = len(tokens) / len(sentence_list) + 0.000001
    return round(average_sent_length)

# Calculating percentage of complex word 
def percentage_complex_word(text):
    stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(plural) for plural in tokens]
    complexWord = 0
    complex_word_percentage = 0
    
    for word in tokens:
        vowels=0
        if word.endswith(('es','ed')):
            pass
        else:
            for w in word:
                if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
                    vowels += 1
            if(vowels > 2):
                complexWord += 1
    if len(tokens) != 0:
        complex_word_percentage = complexWord/len(tokens)
    
    return complex_word_percentage

# calculating Fog Index 
def calculate_fog_index(averageSentenceLength, percentageComplexWord):
    fogIndex = 0.4 * (averageSentenceLength + percentageComplexWord)
    return round(fogIndex,3)


def calculate_cosine(data_dict, gold_standard_tokens):
    """"data: type dataframe"""
    cosine_similarity = []
    for doc in data_dict.keys():
        tokens = word_tokenize(doc)
        cosine_similarity.append(textdistance.cosine.similarity(gold_standard_tokens , tokens))
    return cosine_similarity

def calculate_entropy(data_dict, gold_standard_tokens):
    """"data: type dataframe"""
    entropy_similarity = []
    for doc in data_dict.keys():
        tokens = word_tokenize(doc)
        entropy_similarity.append(textdistance.entropy_ncd.similarity(gold_standard_tokens , tokens))
    return entropy_similarity

