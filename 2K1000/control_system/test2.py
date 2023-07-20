import smtplib  # 导入smtplib库，用于发送邮件
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

conn = smtplib.SMTP("smtp.qq.com")
conn.login('2786502479@qq.com', 'dyxnxaqigbmudfge')  # 参数二：授权码

# text = MIMEText('温度过高警告', 'plain', 'UTF-8')  # 邮件内容
# mail.attach(text)  # 将邮件内容加入
# 发送邮件
# conn.sendmail('2789539492@qq.com', '1353890723@qq.com', mail.as_string())

tem = 41
hum = 40
fire = 1
tem_str = '温度过高警告，' + '当前温度为：' + str(tem)
hum_str = '湿度过低警告，' + '当前湿度为：' + str(hum)
fire_str = '烟雾浓度过高警告，注意检查周围环境，避免发生火灾'


def mail_info(mail):
    theme = Header("传感器报警", "UTF-8").encode()  # 主题对象
    mail['Subject'] = theme  # 邮件主题
    mail['From'] = '2786502479@qq.com'  # 发件人
    mail['To'] = '2569882124@qq.com'  # 收件人


def tem_alarm():
    mail = MIMEMultipart()  # 邮件对象
    mail_info(mail)
    text = MIMEText(tem_str, 'plain', 'UTF-8')  # 邮件内容
    mail.attach(text)  # 将邮件内容加入
    conn.sendmail('2786502479@qq.com', '2569882124@qq.com', mail.as_string())
    print("温度过高警告")


def hum_alarm():
    mail = MIMEMultipart()  # 邮件对象
    mail_info(mail)
    text = MIMEText(hum_str, 'plain', 'UTF-8')  # 邮件内容
    mail.attach(text)  # 将邮件内容加入
    conn.sendmail('2786502479@qq.com', '2569882124@qq.com', mail.as_string())
    print("湿度过低警告")


def fire_alarm():
    mail = MIMEMultipart()  # 邮件对象
    mail_info(mail)
    text = MIMEText(fire_str, 'plain', 'UTF-8')  # 邮件内容
    mail.attach(text)  # 将邮件内容加入
    conn.sendmail('2786502479@qq.com', '2569882124@qq.com', mail.as_string())
    print("烟雾浓度过高警告")


if __name__ == '__main__':
    if tem > 40:
        tem_alarm()
    if hum < 40:
        hum_alarm()
    if fire == 1:
        fire_alarm()
# conn.sendmail('2786502479@qq.com', '2569882124@qq.com', mail.as_string())
# print("okay")
# 关闭连接
conn.quit()
