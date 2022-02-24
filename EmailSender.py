import smtplib
from email.mime.text import MIMEText
import re

USERNAME = 'spydir1209'
ADDRESS = 'spydir1209@gmail.com'
PASSWORD = 'adicyber109'
BODY = 'Hello ip is {ip} \n this is the change:{message}'
SUBJECT = 'SpyDir'


def create_mail(receiver_address, ip, message):
    try:
        body = BODY.format(ip=ip, message=message)
        msg = MIMEText(body)
        msg['Subject'] = SUBJECT
        msg['From'] = ADDRESS
        msg['To'] = receiver_address
        msg = msg.as_string()
        return msg
    except:
        pass


def send_email(receiver_address, ip, message):
    try:
        msg = create_mail(receiver_address, ip, message)  # Create SMTP body
        if not msg:
            return False
        # Send through SMTP Gmail server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Connect SMTP Server
        server.ehlo()
        server.login(USERNAME, PASSWORD)
        server.sendmail(ADDRESS, receiver_address, msg)
        server.close()
    except:
        pass


send_email('adi.soco.109@gmail.com')
