import time
import requests
import json
from gen_csv import write_file


def main(hours):
    response = requests.get('http://127.0.0.1:5000/el_panel/find', params={"hours": hours})

    content = response.content.decode()

    origin_data: dict = json.loads(content)
    data_list = origin_data.get("msg")

    if origin_data.get("resno") != '0':
        print(data_list)
        return

    csv_data = [
        [
            '组件条码', '组件过站时间', 'AI 判定结果', 'EL 判定结果', 'AP 判定结果', '扫码机台',
            '不良原因', '不良位置', '人工删减', '单一电池隐裂数', '组件测试次数'
        ]
    ]

    for data in origin_data.get('msg'):
        filed = list()
        if data.get('barcode') == '0':
            continue
        filed.append(data['barcode'])
        filed.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['create_time'])))
        judge_res = data['status']
        for i in judge_res:
            if i['by'] == 'AI':
                filed.append(i['result'])
                assert len(filed) == 3
            if i['by'] == 'OP':
                filed.append(i['result'])
                assert len(filed) == 4
        filed.append(data['ap_result'])  # ap 判定结果
        filed.append(data['el_no'])  # 扫码机台

        # 不良原因 和 不良位置
        many_cracks = dict()
        if not data['defects']:
            filed.append('N/A')  # 不良原因
            filed.append('N/A')
            filed.append('N/A')  # 人工删减
            filed.append('N/A')  # 单一电池隐裂数目
        else:
            for defect in data['defects']:
                if defect["by"] != 'AI':
                    continue
                form = defect['type']
                position = defect['position']["c"]
                deleted = 'Y' if defect["status"] == 'true' else 'N'
                if not many_cracks.get(f'{form}#{position}#{deleted}'):
                    many_cracks[f'{form}#{position}#{deleted}'] = 0
                many_cracks[f'{form}#{position}#{deleted}'] += 1

        char_lists = list()
        for key, value in many_cracks.items():
            char_li = key.split('#')
            print("#######", char_li)
            char_li.append(value)
            print("!!!!!", char_li)
            if len(filed) == 6:
                filed += char_li
                print("@@@@@@@@", filed)
            else:
                char_li = ['', '', '', '', '', ''] + char_li
                char_lists.append(char_li)

        filed.append(data['times_of_storage'])  # 组件测试次数
        csv_data.append(filed)
        for i in char_lists:
            csv_data.append(i)

    write_file(csv_data)
    print('OK')


if __name__ == '__main__':
    main(48)
