import csv
#izveidojam funkciju
def read_field(file_name, i=0):
    with open(file_name) as f:
        csv_reader = csv.reader(f)
        result = []
        for row in csv_reader:
            result.append(row[i])
        return result
#nolasam failus
a = read_field('saraksts_1.csv', i=2)
b = read_field('saraksts_2.csv', i=2)
#aprēķinam datus
c = a+b
d = (len(c)-len(a)) + (len(c)-len(b))
c = list(set(c))
#izvadam datus
print(f'Tikai 1.semināru apmeklēja {len(c)-len(b)} cilvēku')
print(f'Tikai 2.semināru apmeklēja {len(c)-len(a)} cilvēku')
print(f'Abus seminārus apmeklēja {d - len(c)} cilvēku')

