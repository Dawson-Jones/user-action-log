import json

a = {
    'spacing between cell or string NG': '串_片间距', 'Membrane migration': '膜偏', 'string dislocation': '错位',
    'foreign matter': '异物', 'VI broken cell': '外观破片', 'barcode NG': '条码贴反', 'Ribbon excess': '焊带未剪',
    'VI others': '外观其他', 'Ribbon migration': '焊带偏移', 'color difference': '色差', 'creepage distance': '隔离不到位'
}

print(json.dumps(a))
# with open('test.json') as f:
