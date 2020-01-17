#!/usr/bin/python
import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub('<.*?>', ' ', text)
    text = re.sub('\w*\d\w*', ' ', text)
    text = re.sub('[‘’“”…]', ' ', text)
    text = re.sub('\[.*?\]', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = text.strip('\n').replace('\n','')
    text = text.strip('\t').replace('\t','')
    text = text.replace('\xa0','')
    text = ' '.join(word for word in text.split() if len(word)>2)
    return text


def removeStopWords(text, stopwords_list):
    text = text.lower()
    for item in stopwords_list:
        text = text.replace(" " + item.lower() + " "," ")
        text = text.replace(" " + item.lower() + ","," ")
        text = text.replace(" " + item.lower() + "."," ")
        text = text.replace(" " + item.lower() + ";"," ")
    text = text.replace("+","")
    return text

def clean_data_dict(dict_data, stopwords):
    """args: dict_data dict form, stopwords list form """
    for i in dict_data.keys():
        text = dict_data[i]
        text = clean_text(text)
        text = removeStopWords(text, stopwords)
        dict_data[i] = text
    return dict_data