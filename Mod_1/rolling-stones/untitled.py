import functions
import csv

with open('data.csv') as f:
    reader = list(csv.DictReader(f))

print(functions.find_by_name(reader, 'Pet Sounds'))
