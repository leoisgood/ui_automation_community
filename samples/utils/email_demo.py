#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/7/25 14:29
# @E-mail: leo.liu@italki.com
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.path.dirname(__file__)
dri_path = os.path.join(current_path, '..\\..', 'reports\\禅道自动化测试报告V1.8\\禅道自动化测试报告V1.8.zip')

smtp_server = 'smtp.qq.com'  # 邮件服务器地址
smtp_sender = '1178472868@qq.com'  # 邮箱名
smtp_senderpassword = 'sqlwuyxincslihic'  # 授权码
smtp_receiver = 'leo.liu@italki.com'  # 收件人
smtp_cc = 'nash86097@gmail.com,curryfor30leo@gmail.com'  # 抄送人
smtp_subject = 'Web自动化测试报告（italki测试版）'  # 邮件主题
smtp_body = 'italki web 自动化测试报告'  # 邮件正文
smtp_file = dri_path

# msg = MIMEText(smtp_body, "html", "utf-8")  # 邮件信息对象
# msg['from'] = smtp_sender
# msg['to'] = smtp_receiver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject
msg = MIMEMultipart()  # 文件的形式发送Email
with open(smtp_file, 'rb') as f:
    # / Users / liuqingjun / PycharmProjects / PO_UI_Test_Framework /reports/禅道自动化测试报告V1.8/禅道自动化测试报告V1.8.zip
    mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])    #
    mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', smtp_file.split('/')[-1]))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg.attach(MIMEText(smtp_body, "html", "utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)  # 465
    smtp.login(user=smtp_sender, password=smtp_senderpassword)
    smtp.sendmail(smtp_sender, smtp_receiver.split(',') + smtp_cc.split(','), msg.as_string())
    print("邮件发送成功")

except smtplib.SMTPException as e:
    print("邮件发送失败,原因是 %s " % e.__str__())
