import sqlite3
import time


# 打开数据库连接
def connect_database():
    conn = sqlite3.connect('test.db')
    return conn


# 获取表名
def get_table_name():
    # table_name = time.strftime("D%Y_%m_%d", time.localtime())
    # return table_name
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 查询最新生成的数据库表名
    sql = "select name from sqlite_master where type = 'table' and name != 'device' order by name desc limit 1;"
    try:
        cursor.execute(sql)
        ret1 = cursor.fetchone()
        ret = ret1[0]
        # 关闭数据库连接
        cursor.close()
        conn.close()
        return ret
    except Exception as e:
        print(e)


# 创建表
def create_table(table_name):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql_drop = 'drop table if exists ' + table_name
    sql_drop_device = 'drop table if exists device'
    # cursor.execute(sql_drop)
    sql_create = 'create table if not exists ' + table_name + '(id int,addr varchar(50),' \
                                                              'day date,' \
                                                              'time date,' \
                                                              'temp double,' \
                                                              'humi int,' \
                                                              'fire_alarm int,' \
                                                              'press int,' \
                                                              'light double,' \
                                                              'gps varchar(55))'
    sql_create_device = 'create table if not exists device (device_id int, online bool);'
    # 异常处理
    try:
        # 创建一个表格
        cursor.execute(sql_create)
        cursor.execute(sql_create_device)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.execute(sql_drop)
        cursor.execute(sql_drop_device)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 插入数据
def insert(table_name, data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 插入一条记录
    sql_insert = 'insert into ' + table_name + '(id,addr,day,time,temp,humi,fire_alarm,press,light,gps) values (?,?,?,?,?,?,?,?,?,?)'
    try:
        cursor.execute(sql_insert, data)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 插入设备数据
def insert_device(dev):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql_insert = 'insert into device(device_id,online) values(?,?)'
    try:
        cursor.execute(sql_insert, dev)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 根据字段名查询数据
def select(table_name, column_name):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'select ' + column_name + ' from ' + table_name + ' where time = (select max(time) from ' + table_name + ' where day = (select max(day) from ' + table_name + '))'
    try:
        cursor.execute(sql)
        ret1 = cursor.fetchall()
        ret = ret1[0][0]
        # 关闭数据库连接
        cursor.close()
        conn.close()
        return ret
    except Exception as e:
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)
        return None


# 查询MAC地址
def select_addr(table_name):
    return select(table_name, 'addr')


# 查询电量
# def select_power(table_name):
#     return select(table_name, 'power')


# 查询年月日
def select_day(table_name):
    return select(table_name, 'day')


# 查询时分秒
def select_time(table_name):
    return select(table_name, 'time')


# 查询温度
def select_temp(table_name):
    return select(table_name, 'temp')


# 查询湿度
def select_humi(table_name):
    return select(table_name, 'humi')


# 查询火警标志位
def select_fire_alarm(table_name):
    return select(table_name, 'fire_alarm')


# 查询气压
def select_press(table_name):
    return select(table_name, 'press')


# 查询光强
def select_light(table_name):
    return select(table_name, 'light')


# 查询经纬度
def select_gps(table_name):
    return select(table_name, 'gps')


# 查询经度
def select_lon(table_name):
    gps = select_gps(table_name)
    lon_str = gps[:gps.index('&')]
    return float(lon_str)


# 查询纬度
def select_lat(table_name):
    gps = select_gps(table_name)
    lat_str = gps[gps.index('&') + 1:]
    # lat = lat_str[:lat_str.index('.')]
    return float(lat_str)


# 查询设备id是否存在
def select_device(dev_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'select * from device where device_id = ' + dev_id + ';'
    try:
        cursor.execute(sql)
        ret = cursor.fetchall()
        if ret:
            return False
        else:
            return True
    except Exception as e:
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 查询设备是否在线
def select_device_online(dev_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'select online from device where device_id = '+dev_id
    try:
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret:
            if ret[0] == 1:
                return "在线"
            else:
                return "离线"
        else:
            print("select_device1()查询失败")
    except Exception as e:
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)



# # 查询RFID信息
# def select_rfid(table_name):
#     return select(table_name, 'rfid')


# # 查询校验码
# def select_verify(table_name):
#     return select(table_name, 'verify')


# 修改数据
def update(table_name, column_name, column, line_name, line_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    line = (line_name, line_id)
    sql_update = 'update ' + table_name + ' set ' + column_name + '=? where ' + column + ' =?'
    try:
        cursor.execute(sql_update, line)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        # 进行回滚
        conn.rollback()
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 修改设备是否在线
def update_device(dev_id, status):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'update device set online = ' + status + ' where device_id = ' + dev_id
    try:
        cursor.execute(sql)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        # 进行回滚
        conn.rollback()
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 修改设备全部离线
def update_device_offline():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'update device set online = FALSE '
    try:
        cursor.execute(sql)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        # 进行回滚
        conn.rollback()
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 删除数据
def delete(table_name, column_name, column):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql_delete = 'delete from ' + table_name + ' where ' + column_name + ' =?'
    column = (column,)
    try:
        cursor.execute(sql_delete, column)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)

# if __name__ == '__main__':
#     print(get_table_name())
