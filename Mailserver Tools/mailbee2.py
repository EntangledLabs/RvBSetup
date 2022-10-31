import smtplib, ssl, getpass, argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtp_server = '172.16.110.17'
smtp_port = 587

test_recv_addr = 'greenteam@beehive.main'

def mail_bees(msg_path, scheme=None, attachment=None):
    '''adminbees = list()
    for i in range(1,int(os.getenv("NUMBEES"))+1):
        adminbees.append('adminbee{}@beehive.main'.format(i))'''
    
    with open(msg_path, "r+") as mail:
        body = mail.readlines()

    msg = MIMEMultipart('mixed')
    sender = body[0].strip('\n')

    msg['From'] = sender
    msg['Subject'] = body[1].strip('\n').split(' ',1)[1]
    
    temp = ""
    for line in body[2:]:
        temp = "{}{}\n".format(temp, line)
    
    if scheme == None:
        msg.attach(MIMEText(temp))
    elif scheme.lower() == 'html':
        msg.attach(MIMEText(temp, 'html'))

    if not attachment == None:
        try:
            with open(attachment, "rb") as attached:
                p = MIMEApplication(attached.read(),_subtype="pdf")	
                p.add_header('Content-Disposition', "attachment; filename= %s" % attachment.split("\\")[-1]) 
                msg.attach(p)
        except Exception as e:
            print(str(e))

    context = ssl._create_unverified_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(sender, getpass.getpass())
        server.sendmail(sender, test_recv_addr, msg.as_string())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Send mail to all of the bees")
    parser.add_argument('mail_path')
    parser.add_argument('-s', '--scheme', default=None, choices=[None, 'html', 'HTML'])
    parser.add_argument('-a', '--attachment', default=None)

    args = parser.parse_args()
    mail_bees(args.mail_path, args.scheme, args.attachment)