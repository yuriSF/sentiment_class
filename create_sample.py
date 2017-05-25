import csv
import pickle
import random
from file_ops import open_file, open_csv

def separate_set(num):
    # training set: num = 1
    # testing set: num = 2
    # developmment set: num = 3
    new_data = []
    for row in data:
        for row_split in data_split:
            cl = row_split.split(',')[1].strip()
            sent_id = row_split.split(',')[0]
            if row[1] == sent_id and cl == num:
                new_row = [row[0], row[1], row[2]]
                new_data.append(new_row)
    return new_data

data = open_csv('results/sent_corpus.csv')
data_split = open_file('treebank/datasetSplit.txt')
_set = separate_set('2')
with open("results/test_set.csv", 'wb') as csvfile:
    csv.writer(csvfile).writerows(_set)
pickle.dump(data, open("results/test_set.p", 'wb'))


"""
#randomizing sample
rts = random.sample(ts, 50)
with open("train_set_random.csv", 'wb') as csvfile:
    csv.writer(csvfile).writerows(rts)
"""
