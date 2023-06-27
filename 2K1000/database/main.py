import db
import time
import uart
import data_parse as d
import threading
from queue import Queue
import export_data


def main():
    # 表名
    table_name = time.strftime("D%Y_%m_%d", time.localtime())
    q = Queue()
    # 创建线程t1来接收数据
    t1 = threading.Thread(target=uart.recv_data, args=(q,))
    # 启动线程
    t1.start()
    # json_str = '{"A":"start","B":"00:01:1B:FF:FF:FF","C":"100","D":["2023","05","06"],"E":["16", "26", "25"],"F":{"F1":"23.02","F2":"26","F3":"0","F4":"26&12&98","F5":"112.342473&16.842207"},"G":"12345678","H":"end"}'
    while True:
        #str = uart.recv_data()
        str1 = q.get()
        print(str1)
        str2 = str1.decode("utf-8")
        print(str2)
        flag = isinstance(str2, str)
        try:
            if flag:
                json_str = eval(str2)
                d_list = d.data_parse(json_str)
                # 判断数据是否完整
                if d_list[0] == "start" and d_list[len(d_list) - 1] == "end":
                    # 删除头部和尾部
                    del d_list[0]
                    del d_list[len(d_list) - 1]
                    # 设置日期为当前的时间
                    d_list[2] = time.strftime("%Y-%m-%d", time.localtime())
                    d_list[3] = time.strftime("%H:%M:%S", time.localtime())
                    # 将列表转为元组
                    data = tuple(d_list)
                    # 创建表
                    db.create_table(table_name)
                    # 将接收到的数据插入表中
                    db.insert(table_name, data)
                    ret = db.select_time(table_name)
                    if ret:
                        print(ret)
            # 将数据库中的数据导出为excel
            export_data.export_excel()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
