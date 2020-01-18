import re
import time


while True:
    ini = input('xxx: ')
    ret = re.match(r'\d{4}-(0?[1-9]|1[0-2])-(([012])?\d|3[01]) (([01])?\d|2[0-3]):[0-5]\d:[0-5]\d$', ini)
    if ret:
        print('ok')
        time_stamp = time.mktime(time.strptime(ini, '%Y-%m-%d %H:%M:%S'))
        print(time_stamp)
    else:
        print('no')
