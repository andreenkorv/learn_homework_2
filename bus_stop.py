import csv

with open('bus_stops.csv', 'r', encoding='pt154') as f:
    fields = ['ID', 'Name', 'Longitude', 'Latitude', 'Street', 'AdmArea']
    reader = csv.DictReader(f, fields, delimiter=';')
    max_count = 0
    list_of_streets = []
    for row in reader:
        list_of_streets.append({"Street": row['Street']})
    street_dict_with_count = {
        element['Street']: list_of_streets.count(element) for element in list_of_streets
    }
    print(f'Всего остановок:{len(list_of_streets)}')
    for key in street_dict_with_count:
        if street_dict_with_count[key] > max_count:
            max_count = street_dict_with_count[key]
            max_bus_stops_street = key
    print(f'Улица: {max_bus_stops_street}, остановок: {max_count}')
