import smtplib
from email.message import EmailMessage

smtp_username = ''
smtp_password = ''
smtp_server = 'localhost'
smtp_port = 1025

msg = EmailMessage()
msg['From'] = 'sender@gmail.com'
msg['To'] = 'receiver@gmail.com'
msg['Subject'] = 'Test Email'
msg.set_content('This is a test email sent from Python.')

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.send_message(msg)
    print('Email sent successfully!')