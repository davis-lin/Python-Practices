import smtplib,os,sys
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

to = 'linar@garena.com'
user = 'admin@garena.com'
pwd = 'ade6RpbV1Dhozb7QPXakDQ'
smtpserver = smtplib.SMTP('smtp.mandrillapp.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(user, pwd)

header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:testing \n'
print(header)

msg = header + '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(user, to, msg)

print('done!')
smtpserver.close()