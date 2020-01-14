import csv
import time


def write_file(csv_data, name):
    with open('./%s.csv' % name, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)


