import pickle
from file_ops import open_csv, write_csv_row
from vectorize import tokenize_sent, get_sent_vector

def main():
    data = open_csv('results/trainset_converted.csv')
    for i, row in enumerate(data[1:]):
        sent = row[2]
        sent_tokens = tokenize_sent(sent)
        sent_vector = get_sent_vector(sent_tokens)
        row[6] = sent_vector
        write_csv_row('results/trainset_vectors300_large.csv', row)
        print i
    pickle.dump(data, open("results/trainset_vectors300_large.p", 'wb'))

main()
