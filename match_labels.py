import csv
import pickle
from file_ops import open_file, open_csv

def match():
    for row in data[1:]:
        row.append('')
        row.append('')
        row.append('')
        for line in labels:
            label_id = line.split('|')[0]
            label_score = line.split('|')[1].strip()
            if label_id == row[0]:
                row[3] = label_score
                label_score = float(label_score)

                if label_score <= 0.2:
                    five_scale = 'very negative'
                if label_score <= 0.4 and label_score > 0.2:
                    five_scale = 'negative'
                if label_score <= 0.6 and label_score > 0.4:
                    five_scale = 'neutral'
                if label_score <= 0.8 and label_score > 0.6:
                    five_scale = 'positive'
                if label_score <= 1 and label_score > 0.8:
                    five_scale = 'positive'

                if label_score <= 0.33:
                    three_scale = 'negative'
                if label_score <= 0.66 and label_score > 0.33:
                    three_scale = 'neutral'
                if label_score <= 1 and label_score > 0.66:
                    three_scale = 'positive'

                row[5] = three_scale
                row[4] = five_scale

                if row[4] != row[6]:
                    row

data = open_csv("results/human_judgments.csv")
labels = open_file("treebank/sentiment_labels.txt")
match()
with open("results/human_judgments_ground.csv", 'wb') as csvfile:
    csv.writer(csvfile).writerows(data)
pickle.dump(data, open("results/test_set_scores.p", 'wb'))
