import time
hw = False
fan = False
count = 0


def temp_control(ser, d_list):
    global hw, fan, count
    tem = d_list[4]
    target_tem = float(37)
    # while True:
    #     ser.write(b'01010100')  # 关闭电热丝
    #     ser.write(b'01010000')  # 关闭风扇
    # while True:
    #     ser.write(b'01010000')  # 打开风扇
    #     time.sleep(5)
    if float(tem) < target_tem:
        # ser.write(b'01010101')  # 打开电热丝
        if fan or hw == False:
            print("关闭风扇")
            ser.write(b'01010000')  # 关闭风扇
            fan = False
            print("打开电热丝")
            hw = True
    elif float(tem) > target_tem:
        if fan == False or hw:
            print("打开风扇")
            ser.write(b'01010011')  # 打开风扇
            fan = True
            print("关闭电热丝")
            ser.write(b'01010100')  # 关闭电热丝
            hw = False
    else:
        # ser.write(b'01010100')  # 关闭电热丝
        print("关闭电热丝")
        hw = False
        ser.write(b'01010000')  # 关闭风扇
        fan = False
