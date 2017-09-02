# -*- coding: UTF-8 -*-  

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTPSenderRefused

class ReMailer():
    
    def send(self):
        sender = '@163.com'
        receiver = '@gmail.com'
        subject = '这是一个测试邮件'
        smtpserver = 'smtp.163.com'
        username = ''
        password = '' 
        
        msg = MIMEText('你好','plain','utf-8')
        msg['Subject'] = Header(subject, 'utf-8') 
        msg['From'] = sender
        msg['To'] = receiver
        
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.set_debuglevel(1)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        
test = ReMailer()
test.send()