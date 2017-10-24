from realE.reCollector import ReCollector
from config.configData import configData
from mail.mailer import Mailer
import time

config = configData('../config.json')

rc = ReCollector(input('lj account'), input('lj pw'))

xiaoqu_links = rc.get_re_list()
re_list = rc.get_re_msg(xiaoqu_links)

for line in re_list:
    print(line)

'''
sender = input('163 account')
passwd = input('163 pw')
smtpServer = "smtp.163.com"

mailer = Mailer(sender, passwd, smtpServer)

receiver = ['@gmail.com', '@qq.com']
subject = "链家每日推送" + time.asctime( time.localtime(time.time()) )
message = ""
for msg in re_list:
    message += (msg + "\n\n")

message = mailer.setMsg(receiver, subject, message)

mailer.send(message)
'''