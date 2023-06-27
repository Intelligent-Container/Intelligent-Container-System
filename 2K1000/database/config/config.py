import os
import db
# 获取当前文件的绝对路径
current_file = os.path.abspath(__file__)
# print(current_file)
# 获取当前文件所在目录
current_dir = os.path.dirname(current_file)
# print(current_dir)
# 获取当前文件所在项目
current_obj = os.path.dirname(current_dir)
# print(current_obj)
# 获取测试数据的所在目录
config_dir = os.path.join(current_obj, 'data')
# 获取数据文件的绝对路径
config_file = os.path.join(config_dir, db.get_table_name()+'.xls')
# print(config_file)