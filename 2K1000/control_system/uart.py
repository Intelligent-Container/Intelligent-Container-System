import serial
import time
import logging
import db
import threading
import os
from config.config import config_dir
import upload_excel as ft

ser = serial.Serial('/dev/ttyS3', 115200, timeout=1)  # '/dev/ttyS3'对应龙芯派 55pin为UART5_TX，56pin为UART5_RX，57和58pin为GND
# ser = serial.Serial('COM3', 115200, timeout=1)  # “COM1”是Windows的串口
# 获取文件夹下的所有文件
files = os.listdir(config_dir)
# 获取文件夹下最新生成的文件
newest_file = max(files, key=lambda x: os.path.getmtime(os.path.join(config_dir, x)))
excel_filename = config_dir + "/" + newest_file
# 配置日志输出的格式和级别
logging.basicConfig(filename='device_status.log', level=logging.INFO, format='%(asctime)s - %(message)s')
# 模拟1B200开发板的上线和下线状态
board_online = [False]
for x in range(10):
    board_online.append(False)
# 存储开发板状态的字典
board_status = {}
time_count = 0
# 记录每一次接收到数据的时间
board_time = [0]
for x in range(10):
    board_time.append(time_count)
count = [0]
for x in range(10):
    count.append(0)

# 在线设备列表
online_list = []


def timer():
    global time_count
    time_count += 1
    # 设置定时器，每秒执行一次
    timer1 = threading.Timer(1, timer)
    timer1.start()


def split_string(string):
    return [string[i:i + 2] for i in range(0, len(string), 2)]


def online(st_sensor, client, ftp):
    global board_online, count, board_time, board_status, online_list
    data = split_string(st_sensor.strip('a').strip('\r\n'))
    # data = st_sensor.strip('\r\n').strip('a').split(":")
    length = len(data)
    if length != 1:
        num = int(data[length - 1], 16)
        # 记录此设备的最新上线时间
        board_time[num] = time_count
        # 判断设备上线
        if not board_online[num]:
            # 判断是1B设备
            if data[0] == "02":
                count[num] = 0

                client.send_message("WillMsg", 'online=' + str(num))
                print("1B200", num, "号设备上线了")
                logging.info("1B200-%d号设备上线了", num)
                ft.upload_file(ftp, newest_file, excel_filename)
                # 将该设备添加到在线列表中
                online_list.append(num)
                # 修改设备的在线状态
                board_online[num] = True
                # 更新此设备在数据库中为在线
                db.update_device(str(num), str(board_online[num]))

                dev = (num, board_online[num])
                if db.select_device(str(num)):
                    db.insert_device(dev)
                # 更新开发板状态
                board_status[num] = board_online[num]
                # 判断是2K设备
            elif data[0] == "01":
                print("2K1000LA", num, "号设备上线了")
                logging.info("2K1000LA-%d号设备上线了", num)
            else:
                print("设备地址错误")


def recv_data(q, client, ftp):

    # 打开串口
    # ser = serial.Serial('COM5', 115200, timeout=1)  # “COM1”是Windows的串口
    # ser = serial.Serial('/dev/ttyS1', 9600, timeout=1) # '/dev/ttyS1'对应龙芯派 8pin为UART3_TX，10pin为UART3_RX，9pin为GND
    # ser = serial.Serial('/dev/ttyS2', 9600, timeout=1) # '/dev/ttyS2'对应龙芯派 53pin为UART4_TX，54pin为UART4_RX，57和58pin为GND
    # 启动定时器
    timer()
    ser.flushInput()
    ser.flushOutput()
    # 接收数据并发送回去
    while True:
        time.sleep(0.02)
        data = ser.readline()
        for key in board_status.keys():
            if time_count - board_time[key] > 5 and board_online[key]:
                print("1B200", key, "号设备下线了")
                client.send_message("WillMsg", 'offline=' + str(key))
                logging.info("1B200-%d号设备下线了", key)
                board_online[key] = False
                board_status[key] = False
                db.update_device(str(key), str(board_online[key]))
                count[key] = 1
                online_list.remove(key)
        if len(data) > 2:
            st_sensor = data.decode('utf-8').strip('\r\n')
            # print(st_sensor)
            if st_sensor.startswith('a'):
                if len(st_sensor) < 16:
                    # 判断设备上线情况
                    online(st_sensor, client, ftp)
                q.empty()
                ser.flushInput()
                ser.flushOutput()
            else:
                q.empty()
                # 保证数据长度
                if 153 > len(st_sensor) >= 151:
                    q.put(st_sensor)
                ser.flushInput()
                ser.flushOutput()
