# How to send lots of email
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'Hero Of Python'
email['to'] = 'ridoyroycse53engg@gmail.com', 'hridoy464@gmail.com'
email['subject'] = '1M Dollar!'

email.set_content(html.substitute({'name': 'Hridoy'}), 'html')

with smtplib.SMTP(host= 'smtp.gmail.com', port= '587') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('banglakontho24mailbox@gmail.com', '!@#123HridoyRoy24')
    smtp.send_message(email)
    print("All is well Boss!")
