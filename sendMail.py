import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_addr = input('Enter your e-mail ID: ')
sender_pass = input('Enter your password: ')
receiver_addr = input("Enter receiver's e-mail ID: ")


message = MIMEMultipart()
message['From'] = sender_addr
message['To'] = receiver_addr
message['Subject'] = input("Enter the subject: ")
message_body = input("Enter your message: ")
message.attach(MIMEText(message_body, 'plain'))


session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_addr, sender_pass)
text = message.as_string()
session.sendmail(sender_addr, receiver_addr, text)
session.quit()

print ('Mail Sent')
