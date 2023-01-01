
import smtplib, ssl
from email.message import EmailMessage







# Create a secure SSL context

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mahir@marketseon.com"  # Enter your address
receiver_email = "info@marketseon.com"  # Enter receiver address
password = "xarnelgrggpzthaq"

msg = EmailMessage()
msg.set_content("Hello Underworld!")
msg['Subject'] = "Hello Underworld from Python Gmail!"
msg['From'] = sender_email
msg['To'] = receiver_email

context = ssl.create_default_context()

#with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#    server.login(sender_email, password)
#    server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
