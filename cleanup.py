from file_ops import open_csv, write_csv_rows

data = open_csv("results/classified_fine.csv")
for row in data:

    if row[5] == 'negative':
        row[5] = 'somewhat negative'

    if row[7] == 'negative':
        row[7] = 'somewhat negative'

    if row[5] == 'very negative':
        row[5] = 'negative'

    if row[7] == 'very negative':
        row[7] = 'negative'

    if row[5] == 'positive':
        row[5] = 'somewhat positive'

    if row[7] == 'positive':
        row[7] = 'somewhat positive'

    if row[5] == 'very positive':
        row[5] = 'positive'

    if row[7] == 'very positive':
        row[7] = 'positive'


write_csv_rows('results/classified_fine2.csv', data)
