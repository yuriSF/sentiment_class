from sklearn import svm
from sklearn.grid_search import GridSearchCV
import numpy as np
from file_ops import open_csv
import pickle

def find_params(p_file):
    data = pickle.load(open(p_file, 'r'))
    _data = [row for row in data if row[6]!='' and row[4]!='']
    print(len(data))
    print(len(_data))
    parameter_candidates = [
      {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
      {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
    ]

    X = [row[6] for row in _data]
    y = [row[4] for row in _data]

    clf = GridSearchCV(estimator=svm.SVC(), param_grid=parameter_candidates, n_jobs=-1)
    print(clf.fit(X, y))
    print('Best C:',clf.best_estimator_.C)
    print('Best Kernel:',clf.best_estimator_.kernel)
    print('Best Gamma:',clf.best_estimator_.gamma)
    return(('C', clf.best_estimator_.C), ('kernel', clf.best_estimator_.kernel), ('gamma', clf.best_estimator_.gamma))
    return x

find_params("results/trainset_vectors300_large.p")

# if __name__ == 'main':
#     find_params("results/trainset_vectors300.p")
