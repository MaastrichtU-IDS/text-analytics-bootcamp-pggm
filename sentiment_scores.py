#!/usr/bin/python

from nltk.tokenize import word_tokenize, sent_tokenize

def read_dictionary(path):
    file = open(path,'r')
    return file.read().lower().split('\n')

# Generate sentiment scores
def generate_score(text, list_to_compare):
    numWords = 0
    tokens = word_tokenize(text)
    for word in tokens:
        if word in list_to_compare:
            numWords  += 1
    
    cumsum = numWords
    return cumsum

# Calculating polarity score
def polarity_score(positive_score, negative_score):
    pol_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    return pol_score

# Counting total words
def total_word_count(text):
    tokens = word_tokenize(text)
    return len(tokens)

# Calculating Average sentence length 
def average_sentence_length(text):
    sentence_list = sent_tokenize(text)
    tokens = word_tokenize(text)
    average_sent_length = len(tokens) / len(sentence_list) + 0.000001
    return round(average_sent_length)

# Calculating percentage of complex word 
def percentage_complex_word(text):
    tokens = word_tokenize(text)
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