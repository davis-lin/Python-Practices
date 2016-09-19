import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_addr = 'linar@garena.com'
to_addr = 'linar@garena.com'
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Test mail part 2"

body = """A\n \
    B\n \
    C\n"""

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.mandrillapp.com', 587)
server.starttls()
server.login('admin@garena.com', 'ade6RpbV1Dhozb7QPXakDQ')
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.close()