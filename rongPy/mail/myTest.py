from config.configData import configData
from mail.mailer import Mailer
import getpass

config = configData('../config.json')

sender = input("Account?")
passwd = getpass.getpass("Password?")
smtpServer = "smtp.163.com"

mailer = Mailer(sender, passwd, smtpServer)

receiver = 'rogerjoying@gmail.com'
subject = "这是一个测试邮件"
msg = "测试邮件内容"

message = mailer.setMsg(receiver, subject, msg)

mailer.send(message)