import csv


with open('students.csv') as f:
    data = csv.reader(f, delimiter=';')

    print(*data, sep='\n')
