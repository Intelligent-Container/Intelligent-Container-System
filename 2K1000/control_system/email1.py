import smtplib  # 导入smtplib库，用于发送邮件
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def alarm(text_str):
    # 通过创建SMTP对象并指定QQ邮箱的SMTP服务器地址，建立与SMTP服务器的连接。
    conn = smtplib.SMTP("smtp.qq.com")
    conn.login('2786502479@qq.com', 'dyxnxaqigbmudfge')  # 参数二：授权码
    # conn.login('2789539492@qq.com', "bfqaolqpbtqhdhee")

    mail = MIMEMultipart()  # 邮件对象
    theme = Header("传感器报警", "UTF-8").encode()  # 主题对象
    mail['Subject'] = theme  # 邮件主题
    mail['From'] = '2786502479@qq.com'  # 发件人
    mail['To'] = '2569882124@qq.com'  # 收件人
    # mail['From'] = '2789539492@qq.com'  # 发件人
    # mail['To'] = '1353890723@qq.com'  # 收件人

    text = MIMEText(text_str, 'plain', 'UTF-8')  # 邮件内容
    mail.attach(text)  # 将邮件内容加入
    # 发送邮件
    # conn.sendmail('2789539492@qq.com', '1353890723@qq.com', mail.as_string())
    conn.sendmail('2786502479@qq.com', '2569882124@qq.com', mail.as_string())
    print(text_str)
    # 关闭连接
    conn.quit()
