import csv

def read_field(file_name):
    all_rows = []
    with open(file_name) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            all_rows.append(tuple(row))
    return all_rows        


s1 = set(read_field('saraksts_1.csv'))
s2 = set(read_field('saraksts_2.csv'))

tikai_s1 = s1 - s2
tikai_s2 = s2 - s1
abi_s = s1 & s2

header = ['Name', 'Surname', 'e-mail']
with open('saraksts_sertifikatiem.csv', 'wt', newline='\n') as f1:
    csv_writer = csv.writer(f1)
    csv_writer.writerow(header)
    for rinda in abi_s:
        csv_writer.writerow(rinda)
        

header = ['Name', 'Surname', 'e-mail','Workshop']
with open('saraksts_turpinat.csv', 'wt',newline='\n') as f2:
    csv_writer = csv.writer(f2)
    csv_writer.writerow(header)
    for rinda in tikai_s1:
        rinda += (1,)
        csv_writer.writerow(rinda)
    
    for rinda in tikai_s2:
        rinda += (2,)
        csv_writer.writerow(rinda)
