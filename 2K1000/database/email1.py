import smtplib

conn = smtplib.SMTP("smtp.qq.com")

conn.login('2789539492@qq.com',"bfqaolqpbtqhdhee")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

mail = MIMEMultipart()#邮件对象

theme = Header("传感器报警","UTF-8").encode()#主题对象

mail['Subject'] = theme#邮件主题

mail['From'] = '2789539492@qq.com'#发件人

mail['To'] = '1353890723@qq.com'#收件人

text = MIMEText('温度过高警告','plain','UTF-8')#邮件内容
mail.attach(text)#将邮件内容加入

#发送邮件
conn.sendmail('2789539492@qq.com','1353890723@qq.com',mail.as_string())
print("okay")
#关闭连接
conn.quit()