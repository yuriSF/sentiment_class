# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:11:17 2017

@author: yuri
"""

import csv
from file_ops import open_file

def match_phrases_sents():
    first_row = ['phrase_id', 'sent_id', 'sent']
    with open("matched_sents4.csv", 'a') as csvfile:
        csv.writer(csvfile).writerow(first_row)
    for item in dictionary:
        item = item.strip()
        phrase_string = item.split('|')[0]
        phrase_id = item.split('|')[1]
        for sent in sents:
            sent = sent.strip()
            sent_string = sent.split('\t')[1]
            sent_id = sent.split('\t')[0]
            if phrase_string == sent_string:
                row = [phrase_id, sent_id, phrase_string]
                with open("matched_sents4.csv", 'a') as csvfile:
                    csv.writer(csvfile).writerow(row)

sents = open_file('datasetSentences.txt')
dictionary = open_file('dictionary.txt')
match_phrases_sents()

#labels = open_file('sentiment_labels.txt')
#data_split = open_file('datasetSplit.txt')
