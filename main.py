import database
import mailServices

#Calling serivces for E-mail
with mailServices.smtplib.SMTP_SSL(mailServices.smtp_server, mailServices.port, context=mailServices.context) as server:
    mailServices.server.login(mailServices.sender_email, mailServices.password)
    mailServices.server.send_message(mailServices.msg, from_addr=mailServices.sender_email, to_addrs=mailServices.receiver_email)


#Calling database services
resultsFromDatabas = database.cur.execute("SELECT * FROM User")
