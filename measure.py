from file_ops import open_csv
import sys
f = open("summary.txt", "w")
sys.stdout = f

class Results(object):
    def __init__(self, data, label, target, ground):
        self.label = label
        self.tp = len([row for row in data if row[target] == label and row[ground] == label])
        self.tn = len([row for row in data if row[target] != label and row[ground] != label])
        self.fn = len([row for row in data if row[target] != label and row[ground] == label])
        self.fp = len([row for row in data if row[target] == label and row[ground] != label])

    def calc_precision(self):
        try:
            p = float(self.tp) / float(self.tp + self.fp)
        except ZeroDivisionError:
            p = 'division by zero'
        return p


    def calc_recall(self):
        try:
            r = float(self.tp) / float((self.tp + self.fn))
        except ZeroDivisionError:
            r = 'division by zero'
        return r

    def calc_accuracy(self):
        try:
            a = float((self.tp + self.tn)) / float((self.tp + self.tn + self.fp + self.fn))
        except ZeroDivisionError:
            a = 'division by zero'
        return a

    def main(self):
        return self.calc_precision(), self.calc_recall(), self.calc_accuracy()

labels_coarse = ['positive', 'negative', 'neutral']
labels_fine = ['positive', 'somewhat positive', 'neutral', 'somewhat negative', 'negative']

def print_results(f, target, ground, label_set, data_name):
    _data = open_csv(f)
    if label_set == 'coarse':
        labels = labels_coarse
    elif label_set == 'fine':
        labels = labels_fine
    print('DATASET: {}\n'.format(data_name))
    print('CLASSIFICATION SCALE: {}\n'.format(label_set))
    for label in labels:
        print("LABEL: {}".format(label))
        data = Results(_data, label, target, ground)
        precision, recall, accuracy = data.main()
        print('{}: precision {}'.format(label, precision))
        print('{}: recall {}'.format(label, recall))
        print('{}: accuracy {}'.format(label, accuracy))
        print('')
    print '______________________________________________'

print_results('results/classified_fine2.csv', 7, 5, 'coarse', 'treebank test set')
print_results('results/classified_coarse.csv', 7, 4, 'fine', 'treebank test set')
print_results('results/human_judgments3.csv', 7, 5, 'coarse', 'my judgments')
print_results('results/human_judgments3.csv', 6, 4, 'fine', 'my judgments')

f.close()
