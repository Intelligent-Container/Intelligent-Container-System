import serial
import time


def recv_gps(q1):
    # 打开串口
    # ser = serial.Serial('COM11', 9600, timeout=1)  # “COM1”是Windows的串口
    # ser = serial.Serial('/dev/ttyS1', 9600, timeout=1) # '/dev/ttyS1'对应龙芯派 8pin为UART3_TX，10pin为UART3_RX，9pin为GND
    # ser = serial.Serial('/dev/ttyS3', 9600, timeout=1) # '/dev/ttyS2'对应龙芯派 53pin为UART4_TX，54pin为UART4_RX，57和58pin为GND
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # '/dev/ttyS3'对应龙芯派 55pin为UART5_TX，56pin为UART5_RX，57和58pin为GND
    # ser.write(b'$PGKC115,0,0,1,0*2B')
    # 接收数据并发送回去
    while True:
        data = ser.readline()
        if data.startswith(b'$GNGGA'):
            # print(data.decode("utf-8"))
            # 拆分数据行
            # lines = data.decode().split('\r\n')
            # 获取第一行的数据
            # first_line = lines[0]
            first_line = data.decode("utf-8")
            # 提取经度和纬度值
            values = first_line.split(',')
            lon_str = values[4]  # 经度
            lon_num = lon_str.split('.')
            lon_du = lon_num[0][:-2]
            t1 = round(float(lon_num[0][-2:]+'.'+lon_num[1]) / 60.0, 6)
            lon_min = (str(t1)).split('.')[1]
            longitude = lon_du + "." + lon_min  # 经度

            lat_str = values[2]  # 纬度
            lat_num = lat_str.split('.')
            lat_du = lat_num[0][:-2]
            t2 = round(float(lat_num[0][-2:] + '.' + lat_num[1]) / 60.0, 6)
            lat_min = (str(t2)).split('.')[1]
            latitude = lat_du + "." + lat_min  # 经度
            gps = longitude + '&' + latitude
            # time.sleep(2)
            q1.put(gps)

