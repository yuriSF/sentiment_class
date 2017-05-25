from file_ops import open_csv

data = open_csv('results/trainset_vectors300.csv')
print len(data)

data2 = open_csv('results/trainset_converted.csv')
print len(data2)
