import csv
import time


def save_file(data):
    csv_field = [
        ['Date', 'Time', 'UserName', 'ID', 'action']
    ]
    for datum in data:
        # row = list()
        # days, minutes, *_ = split_time(datum['time'])
        row = split_time(datum['time'])  # list have two elements first is Date second is Time
        key_li = list(datum.keys())
        row.append(datum[key_li[1]])
        row.append(datum[key_li[0]])
        row.append(datum['action'])
        csv_field.append(row)

    write_file(csv_field)
    return True


def split_time(time_stamp):
    str_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time_stamp))
    return str_time.split()


def write_file(csv_data):
    with open('./user_action.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)


if __name__ == '__main__':
    split_time(time.time())
