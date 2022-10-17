import os
from smtplib import SMTP

'''
Format for mail files:
<sender>
Subject: <subject>
<body>
'''
def mail_bees(msg_path):
    adminbees = list()
    for i in range(1,int(os.getenv("NUMBEES"))+1):
        adminbees.append('adminbee{}@beehive.main'.format(i))

    with open(msg_path, "r+") as mail:
        msg = mail.readlines()

    sender = msg[0].strip('\n')
    msg = msg[1:]

    temp = ""
    for line in msg:
        temp = "{}{}\n".format(temp, line)
    
    msg = temp
    server = SMTP("localhost")

    for adminbee in adminbees:
        tmp_msg = "To: {}\nFrom: {}\n".format(adminbee, sender) + msg
        server.sendmail(sender, adminbee, tmp_msg)