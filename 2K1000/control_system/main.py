import db
import time
import uart
import data_parse as d
import threading
from queue import Queue
import export_data
import gps
import control as c
from MQTTcli import MQTTClient
import json
import upload_excel as ft
client = MQTTClient(
    client_id="loongsonsd",
    username="loongson",
    password="loongson",
    server="q24a314e.ala.cn-hangzhou.emqxsl.cn",
    port=8883,
    cafile="emqxsl-ca.crt"
)
host = '139.9.232.101'  # IP
port = 21  # 端口
username = 'ftptest'  # 用户名
password = 'JYshn0206'  # 密码
ftp = ft.ftp_connect(host, port, username, password)


def run_mqtt_client(client):
    client.start_loop()

def main():
    # 表名
    table_name = time.strftime("D%Y_%m_%d", time.localtime())
    q = Queue()
    q1 = Queue()
    # 创建线程t3来实现mqtt
    t3 = threading.Thread(target=run_mqtt_client, args=(client,))
    # 启动线程
    t3.start()
    # 创建线程t1来接收传感器数据
    t1 = threading.Thread(target=uart.recv_data, args=(q, client, ftp))
    # 启动线程
    t1.start()
    # # 创建线程t2来接收gps数据
    t2 = threading.Thread(target=gps.recv_gps, args=(q1,))
    # # 启动线程
    t2.start()
    q.empty()
    # json_str = '{"A":"start","B":"00:01:1B:FF:FF:FF","C":"100","D":["2023","05","06"],"E":["16", "26", "25"],"F":{"F1":"23.02","F2":"26","F3":"0","F4":"26&12&98","F5":"112.342473&16.842207"},"G":"12345678","H":"end"}'
    while True:
        # str = uart.recv_data()
        # 接收传感器数据
        str_sensor = q.get()
        print(str_sensor)
        # 判断str_sensor是否是字符串
        flag = isinstance(str_sensor, str)
        # 接收gps数据
        str_gps = q1.get()
        if str_sensor == "":
            flag = False
        try:
            if flag:
                json_str = eval(str_sensor)
                # 将字符串转换为字典
                dic = json.loads(json_str)
                # 在字典中添加新的键值对
                dic['F']['F6'] = str_gps
                dic['D'][0] = time.strftime("%Y", time.localtime())
                dic['D'][1] = time.strftime("%m", time.localtime())
                dic['D'][2] = time.strftime("%d", time.localtime())
                dic['E'][0] = time.strftime("%H", time.localtime())
                dic['E'][1] = time.strftime("%M", time.localtime())
                dic['E'][2] = time.strftime("%S", time.localtime())
                # 将字典转换为字符串
                output_str = json.dumps(dic)
                client.send_message("testtopic", output_str)
                d_list = d.data_parse(json_str)
                # 判断数据是否完整
                if d_list[0] == "start" and d_list[len(d_list) - 1] == "end":
                    # 删除头部和尾部
                    del d_list[0]
                    del d_list[len(d_list) - 1]
                    # get_device_name(d_list)
                    c.temp_control(uart.ser, d_list[0], d_list)
                    # 设置日期为当前的时间
                    d_list[2] = time.strftime("%Y-%m-%d", time.localtime())
                    d_list[3] = time.strftime("%H:%M:%S", time.localtime())

                    d_list[len(d_list) - 1] = str_gps
                    # 将列表转为元组
                    data = tuple(d_list)
                    # 创建表
                    db.create_table(table_name)
                    # 将接收到的数据插入表中
                    db.insert(table_name, data)
            # 将数据库中的数据导出为excel
            export_data.export_excel()
        except Exception as e:
            # print("111")
            print(e)


if __name__ == '__main__':
    db.update_device_offline()
    main()


# def get_device_name(d_list):
#     global board_online, count, board_time, board_status, online_list
#     data = d_list[1].split(':')
#     length = len(data)
#     num = int(data[length - 1], 16)
#     # 记录此设备的最新上线时间
#     # board_time[num] = time.time()
#     board_time[num] = time_count
#     # 判断设备上线
#     if not board_online[num]:
#         # 判断是1B设备
#         if data[0] == "02":
#             count[num] = 0
#             print("1B200", num, "号设备上线了")
#             logging.info("1B200-%d号设备上线了", num)
#             # 将该设备添加到在线列表中
#             online_list.append(num)
#             # 修改设备的在线状态
#             board_online[num] = True
#             # 更新此设备在数据库中为在线
#             db.update_device(str(num), str(board_online[num]))
#
#             dev = (num, board_online[num])
#             if db.select_device(str(num)):
#                 db.insert_device(dev)
#             # 更新开发板状态
#             board_status[num] = board_online[num]
#             # 判断是2K设备
#         elif data[0] == "01":
#             print("2K1000LA", num, "号设备上线了")
#             logging.info("2K1000LA-%d号设备上线了", num)
#         else:
#             print("设备地址错误")

