import xlwt
import db
import copy
from config.config import config_file


# 获取每列的最大列宽
def get_max_col(max_list):
    line_list = []
    # i表示行，j表示列
    for j in range(len(max_list[0])):
        line_num = []
        for i in range(len(max_list)):
            line_num.append(max_list[i][j])# 将每列的宽度存入line_num
        line_list.append((max(line_num)))# 将每列最大宽度存入line_list
    return line_list


# 将数据导出为excel函数
def export_excel():
    conn = db.connect_database()
    cursor = conn.cursor()
    table_name = db.get_table_name()
    sql = 'select * from %s' % table_name
    cursor.execute(sql)
    fields = [field[0] for field in cursor.description]  # 获取所有的字段名
    all_data = cursor.fetchall()
    # 写入excel
    col_list = []  # 记录每列宽度
    col_num = []
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
    for col, field in enumerate(fields):
        sheet.write(0, col, field)
    row = 1
    for data in all_data:
        for col, field in enumerate(data):
            sheet.write(row, col, field)
            col_num.append(len(str(field)))
        col_list.append(copy.copy(col_num))
        row += 1
    # 获取每列最大宽度
    col_max_num = get_max_col(col_list)
    # print(col_max_num)
    # 设置自适应列宽
    for i in range(0, len(col_max_num)):
        sheet.col(i).width = 256 * (col_max_num[i] + 3)
    book.save(config_file)
    # 关闭数据库连接
    cursor.close()
    conn.close()


# if __name__ == '__main__':
#     export_excel()





