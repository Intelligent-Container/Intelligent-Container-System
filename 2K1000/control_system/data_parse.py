import json
import email1

flag1 = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True
flag6 = True


def data_parse(json_str):

    global flag1, flag2, flag3, flag4, flag5, flag6
    obj = json.loads(json_str)
    A = obj['A']  # 报头
    B = obj['B']  # MAC地址
    mac = B.split(':')
    device_num = int(mac[len(mac) - 1], 16)

    num = B.split(':')
    num_str = num[3] + num[4]
    id = int(num_str, 16)
    # C = obj['C']  # 电量

    D0 = obj['D'][0]
    D1 = obj['D'][1]
    D2 = obj['D'][2]

    E0 = obj['E'][0]
    E1 = obj['E'][1]
    E2 = obj['E'][2]
    D = D0 + "-" + D1 + "-" + D2  # 年月日
    E = E0 + ":" + E1 + ":" + E2  # 时分秒
    F1 = obj['F']['F1']  # 温度
    # F1 = temp_str[:temp_str.index('.') + 2]
    F2 = obj['F']['F2']  # 湿度
    F3 = obj['F']['F3']  # 烟雾报警

    tem_str = '温度过高警告\n' + '当前设备为：' + str(device_num) + '号设备\n' + '当前温度为：' + str(F1)
    hum_str = '湿度过低警告\n' + '当前设备为：' + str(device_num) + '号设备\n' + '当前湿度为：' + str(F2)
    fire_str = '烟雾浓度过高警告\n' + '当前设备为：' + str(device_num) + '号设备\n' + '注意检查周围环境，避免发生火灾'
    if device_num == 1:
        if float(F1) > 35:
            if flag1:
                email1.alarm(tem_str)
                flag1 = False
        if int(F2) < 40:
            if flag2:
                email1.alarm(hum_str)
                flag2 = False
        if int(F3) == 1:
            if flag3:
                email1.alarm(fire_str)
                flag3 = False
    if device_num == 2:
        if float(F1) > 35:
            if flag1:
                email1.alarm(tem_str)
                flag4 = False
        if int(F2) < 40:
            if flag2:
                email1.alarm(hum_str)
                flag5 = False
        if int(F3) == 1:
            if flag3:
                email1.alarm(fire_str)
                flag6 = False

    F4 = obj['F']['F4']  # 气压
    F5 = obj['F']['F5']  # 光强

    # G = obj['G']  # RFID信息 暂定16位字符串
    # H = obj['H']  # 校验位
    I = obj['I']  # 停止位

    # checkstr = A + ":" + B + ":" + C + ":" + D0 + ":" + D1 + ":" + D2 + ":" + E0 + ":" + E1 + ":" + E2 + ":" + F1 + ":" + F2 + ":" + F3 + ":" + F4 + ":" + F5 + ":" + F6 + ":" + G + ":" + I
    # checksum = check.calculate_checksum(checkstr)
    # if int(H) == checksum:
    #     print("数据校验成功")
    #     data = [A, B, C, D, E, F1, F2, F3, F4, F5, F6, G, H, I]
    # print(data)
    #     return data
    # else:
    #     print("数据校验失败")
    #     return None
    F6 = "112.23&123.34"  # 经纬度
    data = [A, id, B, D, E, F1, F2, F3, F4, F5, F6, I]
    return data
