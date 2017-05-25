import glob, os
import pickle, csv

def write_csv_rows(f, rows):
    with open(f, 'wb') as csvfile:
        csv.writer(csvfile).writerows(rows)

os.chdir('fine')
data = []
for f in glob.glob('*.p'):
    print f
    row = pickle.load(open(f, 'r'))
    print row
    data.append(row)

os.chdir('..')
write_csv_rows('classified_fine.csv', data)
