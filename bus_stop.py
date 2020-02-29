import csv
from collections import Counter

with open('bus_stops.csv', 'r', encoding='pt154') as f:
    fields = ['ID', 'Name', 'Longitude', 'Latitude', 'Street', 'AdmArea']
    reader = csv.DictReader(f, fields, delimiter=';')
    list_of_streets = []
    for row in reader:
        list_of_streets.append(row['Street'])
    c = Counter(list_of_streets)
    street = c.most_common(1)[0]
    print(f'Улица: {street[0]}; Остановок {street[1]}')
