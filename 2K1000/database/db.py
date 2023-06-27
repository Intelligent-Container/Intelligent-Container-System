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
    sql = "select name from sqlite_master where type = 'table' order by name desc limit 1;"
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
    #cursor.execute(sql_drop)
    sql_create = 'create table if not exists ' + table_name + '(addr varchar(50),' \
                                                              'power int,' \
                                                              'day date,' \
                                                              'time date,' \
                                                              'temp double(4,2),' \
                                                              'humi double(4,2),' \
                                                              'smok int,' \
                                                              'atti varchar(20),' \
                                                              'gps varchar(50),' \
                                                              'verify varchar(20)) '
    # 异常处理
    try:
        # 创建一个表格
        cursor.execute(sql_create)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.execute(sql_drop)
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
    sql_insert = 'insert into ' + table_name + '(addr,power,day,time,temp,humi,smok,atti,gps,verify) values (?,?,?,?,?,?,?,?,?,?)'
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


# 根据字段名查询数据
def select(table_name, column_name):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'select '+ column_name+' from '+table_name +' where time = (select max(time) from '+ table_name + ' where day = (select max(day) from '+table_name+'))'
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


# 查询地址
def select_addr(table_name):
    return select(table_name, 'addr')


# 查询电量
def select_power(table_name):
    return select(table_name, 'power')


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


# 查询烟雾浓度
def select_smok(table_name):
    return select(table_name, 'smok')


# 查询姿态
def select_atti(table_name):
    return select(table_name, 'atti')


# 查询gps
def select_gps(table_name):
    return select(table_name, 'gps')


# 查询校验码
def select_verify(table_name):
    return select(table_name, 'verify')


# 修改数据
def update(table_name, column_name, column, line_name, line_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    line = (line_name, line_id)
    sql_update = 'update '+table_name+' set '+column_name + '=? where '+column+' =?'
    try:
        cursor.execute(sql_update, line)
        conn.commit()
        # 关闭数据库连接
        cursor.close()
        conn.close()
    except Exception as e:
        #进行回滚
        conn.rollback()
        # 关闭数据库连接
        cursor.close()
        conn.close()
        print(e)


# 删除数据
def delete(table_name, column_name, column):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql_delete = 'delete from '+table_name+' where '+column_name+' =?'
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




