from file_ops import open_csv, write_csv_row

# data = open_csv('results/human_judgments3.csv')
# for row in data:
#     if row[7] != row[5] or row[6] != row[4]:
#         write_csv_row('mismatches.csv', row)


data = open_csv('results/classified_coarse.csv')
for row in data:
    if row[6] != row[4]:
        write_csv_row('results/mismatches_testset_coarse.csv', row)

data = open_csv('results/classified_fine2.csv')
for row in data:
    if row[6] != row[4]:
        write_csv_row('results/mismatches_testset_fine.csv', row)
