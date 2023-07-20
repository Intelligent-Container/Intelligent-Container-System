import time
hw = False
fan = False
target_tem = float(20)


def control(ser, num, tem):
    global hw, fan, target_tem
    hex_num = hex(num)[2:].zfill(2).encode('utf-8')
    fan_off = b'01' + hex_num + b'0000'
    fan_on = b'01' + hex_num + b'0011'
    hw_on = b'01' + hex_num + b'0101'
    hw_off = b'01' + hex_num + b'0100'
    # print(type(fire))
    # if fire == '1':
    #     if fan == False or hw:
    #         ser.write(fan_on)
    #         print(num, "打开风扇")
    #         fan = True
    #         print(num, "关闭电热丝")
    #         ser.write(hw_off)
    #         # ser.write(b'01010100')  # 关闭电热丝
    #         hw = False
    # elif fire == '0':
    #     if fan or hw == False:
    #         print(num, "关闭风扇")
    #         ser.write(fan_off)  # 关闭风扇
    #         fan = False
    #         # ser.write(hw_on)
    #         # ser.write(b'01010101')  # 打开电热丝
    #         print(num, "打开电热丝")
    #         hw = True
    if float(tem) < target_tem :

        if fan or hw == False:
            print(num, "关闭风扇")
            ser.write(fan_off)  # 关闭风扇
            fan = False
            # ser.write(hw_on)
            # ser.write(b'01010101')  # 打开电热丝
            print(num, "打开电热丝")
            hw = True
    elif float(tem) > target_tem:
        if fan == False or hw:
            print(num, "打开风扇")
            ser.write(fan_on)  # 打开风扇
            fan = True
            print(num, "关闭电热丝")
            ser.write(hw_off)
            # ser.write(b'01010100')  # 关闭电热丝
            hw = False
    else:
        # ser.write(b'01010100')  # 关闭电热丝
        ser.write(hw_off)
        print(num, "关闭电热丝")
        hw = False
        ser.write(fan_off)  # 关闭风扇
        fan = False


def temp_control(ser, id, d_list):
    global target_tem
    tem = d_list[4]
    # fire = d_list[6]
    if id == 1:
        target_tem = float(32)
        control(ser, id, tem)
    # elif id == 2:
    #     target_tem = float(33)
    #     control(ser, id, tem, fire)
    # while True:
    #     ser.write(b'01010100')  # 关闭电热丝
    #     ser.write(b'01010000')  # 关闭风扇
    # while True:
    #     ser.write(b'01010000')  # 打开风扇
    #     time.sleep(5)
