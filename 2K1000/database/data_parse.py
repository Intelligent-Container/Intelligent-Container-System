import json


def data_parse(json_str):
    obj = json.loads(json_str)
    A = obj['A']  # 报头
    B = obj['B']  # MAC地址
    C = obj['C']  # 电量
    D = obj['D'][0] + "-" + obj['D'][1] + "-" + obj['D'][2]  # 年月日
    E = obj['E'][0] + ":" + obj['E'][1] + ":" + obj['E'][2]  # 时分秒
    temp_str = obj['F']['F1']  # 温度
    F1 = temp_str[:temp_str.index('.') + 2]

    humi_str = obj['F']['F2']  # 湿度
    F2 = humi_str[:humi_str.index('.')]

    smoke_str = obj['F']['F3']  # 烟雾报警
    smoke = int(smoke_str)
    if 5 <= smoke <= 15:
        F3 = 1
    else:
        F3 = 0

    press_str = obj['F']['F4']  # 气压
    F4 = press_str[:press_str.index('.')]

    F5 = obj['F']['F5']  # 经纬度
    G = obj['G']  # RFID信息 暂定16位字符串
    H = obj['H']  # 校验位
    I = obj['I']  # 停止位
    data = [A, B, C, D, E, F1, F2, F3, F4, F5, G, H, I]
    # print(data)
    return data
