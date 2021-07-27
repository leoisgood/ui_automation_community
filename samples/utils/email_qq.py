#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/7/25 12:05
# @E-mail: leo.liu@italki.com
# !/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/7/25 11:31
# @E-mail: leo.liu@italki.com
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

# 第三方 SMTP 服务
mail_host = 'smtp.qq.com'  # 设置服务器
mail_user = "1178472868@qq.com"  # 用户名
mail_pass = "sqlwuyxincslihic"  # 口令
sender = '1178472868@qq.com'
receivers = ['leo.liu@italki.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("leo-qq", 'utf-8')
message['To'] = Header("leo@italki", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e, "Error: 无法发送邮件")