# How to send lots of email
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Hero Of Python'
email['to'] = 'ridoyroycse53engg@gmail.com'
email['subject'] = 'You won 1M Dollars'

email.set_content("I am the Hero of Python!")

with smtplib.SMTP(host= 'smtp.gmail.com', port= '587') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('banglakontho24mailbox@gmail.com', '!@#123HridoyRoy24')
    smtp.send_message(email)
    print("All is well Boss!")
