import requests
import json
from gen_csv import write_file


def combine_list(li: list, *args) -> list:
    for ele in args:
        if isinstance(ele, (list, tuple)):
            li += ele
        else:
            li.append(ele)
    return li


def convert_coord(flag: bool, position: str, amount: int):
    """convert coordinate yc to mes

    flag: True -> el_no belong to ['1', '2', '3']
    position: coordinate string like "1 2" split with space
    amount: how many cells in whole panel

    return: a correct coordinate in mes
    """
    coord_x, coord_y = position.split()
    if flag:
        position = ' '.join([str(7 - int(coord_x)), coord_y])
    else:
        temp_num = amount / 6 + 1
        position = ' '.join([coord_x, str(temp_num - int(coord_y))])

    return position


def load_config():
    # with open('info_map.yaml') as f:
    #     info_map = yaml.load(f, Loader=yaml.Loader)

    info_map = {
        'EL_CODE': {'cr': 'NG隐裂',
                    'mr': 'NG混档',
                    'bc': 'NG失效',
                    'cs': 'NG虚焊',
                    'br': 'NG破片',
                    'bb': 'NG断栅',
                    'Black_Edge_shadow': 'NG黑边',
                    'other': 'NG其他'},
        'VI_CODE': {'spacing between cell or string NG': '串_片间距',
                    'Membrane migration': '膜偏',
                    'string dislocation': '错位',
                    'foreign matter': '异物',
                    'VI broken cell': '外观破片',
                    'barcode NG': '条码贴反',
                    'Ribbon excess': '焊带未剪',
                    'VI others': '外观其他',
                    'Ribbon migration': '焊带偏移',
                    'color difference': '色差',
                    'creepage distance': '隔离不到位'}
    }

    return info_map


def send_http(url, st, et):
    try:
        response = requests.get('http://{}/report'.format(url), params={"start_time": st, 'end_time': et})
    except:
        return False
    if response.status_code != 200:
        return False

    content = response.content.decode()
    origin_data: dict = json.loads(content)

    if origin_data.get("errno") != '0':
        return False
    return origin_data.get('msg')


def make_reports(url, st, et, st_str, et_str):
    csv_data = send_http(url, st, et)
    if csv_data:
        write_file(csv_data, st_str.replace(':', '#') + ' ' + et_str.replace(':', '#'))
        return True
    else:
        return False


if __name__ == '__main__':
    make_reports(1579150000, 1579159685, '2019-8-31', '2020-2-2')
    # load_config()
