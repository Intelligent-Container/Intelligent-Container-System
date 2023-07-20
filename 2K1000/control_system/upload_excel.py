import os
from config.config import config_dir
from ftplib import FTP

"""

可以实现上传 下载单个文件

"""


def ftp_connect(host, port, username, password):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp


"""

从ftp服务器下载文件

remotepath:远程路径
localpath：本地路径

"""


def download_file(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


"""

从本地上传文件到ftp

remotepath:远程路径
localpath：本地路径

"""


def upload_file(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')

    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    host = '139.9.232.101'  # IP
    port = 21  # 端口
    username = 'ftptest'  # 用户名
    password = 'JYshn0206'  # 密码
    ftp = ftp_connect(host, port, username, password)
    # 获取文件夹下的所有文件
    files = os.listdir(config_dir)
    # 获取文件夹下最新生成的文件
    newest_file = max(files, key=lambda x: os.path.getmtime(os.path.join(config_dir, x)))
    excel_filename = config_dir + "\\" + newest_file
    upload_file(ftp, newest_file, excel_filename)
    # download_file(ftp, r"/CMAQ/ftp.log", r"/run/media/test/mydata/data_post/ftp.log")
    ftp.quit()