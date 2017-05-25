from sklearn import svm
from sklearn.grid_search import GridSearchCV
import numpy as np
from file_ops import open_csv, write_csv_row
import pickle
import spacy
from vectorize import tokenize_sent, get_sent_vector

train_data = pickle.load(open("results/trainset_vectors300_large.p", 'r'))
_train_data = [row for row in train_data if row[6]!='' and row[4]!='']
test_data = open_csv('results/test_set_scores_conv.csv')
X = [row[6] for row in _train_data[1:]]
y = [row[5] for row in _train_data[1:]]
clf = svm.SVC(C=100, kernel='rbf', gamma=0.001)
print(clf.fit(X, y))

def classify(sent_vector):
    prediction = clf.predict([sent_vector])
    return prediction[0]

def predict_sample(test_data):
    for i, row in enumerate(test_data):
        row.append('')
        row.append('')
        test_sent = row[2]
        test_tokens = tokenize_sent(test_sent)
        test_vector = get_sent_vector(test_tokens)
        prediction = classify(test_vector)
        row[6] = test_vector
        row[7] = prediction
        #write_csv_row('results/coarse.csv', row)
        pickle_path = '/media/yuri/Extra Drive 2/mya_assignment/stanfordSentimentTreebank/results/fine/' + str(i) + '.p'
        pickle.dump(row, open(pickle_path, "wb"))
        print(i, prediction)
    return test_data

predictions = predict_sample(test_data)
#pickle.dump(test_data, open("results/coarse.p", 'wb'))
