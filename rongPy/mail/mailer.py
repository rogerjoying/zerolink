# -*- coding: UTF-8 -*-  

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Mailer():
    
    def __init__(self, sender, password, server):
        self.sender = sender
        self.password = password
        self.smtpserver = server
          
    def setMsg(self, receiver, subject, msg):        
        message = MIMEText(msg, 'plain', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8') 
        message['From'] = self.sender
        
        if isinstance(receiver, list):
            message['To'] = ",".join(receiver)
        else:
            message['To'] = receiver
            
        return message        
    
    def send(self, msg):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.set_debuglevel(1)
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender, msg['To'], msg = msg.as_string())
        smtp.quit()
        