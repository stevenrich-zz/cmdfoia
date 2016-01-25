import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import csv
import getpass
import datetime

recipient = raw_input("Email address you want to send your FOIA to: ")
user = raw_input("Email username: ")
password = getpass.getpass()
name = raw_input("Your name: ")
organization = raw_input("Your organization: ")
filename = "FOIA" + str(unique_id) + ".pdf"

smtpObj = smtplib.SMTP('m.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(user, password)

to = [str(recipient)]
bcc = [user]
fromAddr = user
subject = "Open records request"
text = "To whom it may concern:\n\nPlease find attached a request under public records law. If you have any questions or concerns, please email me at" + str(user) + ".\n\nThank you,\n\n" +str(name) + "\n" +str(organization) + "\n" + str(user)
emailMsg = MIMEMultipart()
body = MIMEText(text, 'plain')
emailMsg['Subject'] = subject
emailMsg['From'] = fromAddr
emailMsg['To'] = ', '.join(to)
emailMsg['Bcc'] = ", ".join(bcc)
emailMsg.attach(body)

fileMsg = MIMEBase('application','pdf')
fileMsg.set_payload(file(str(filepath)).read())
Encoders.encode_base64(fileMsg)
fileMsg.add_header('Content-Disposition','attachment;filename=' + str(filename))
emailMsg.attach(fileMsg)

tos = to+bcc
smtpObj.sendmail(fromAddr, tos, emailMsg.as_string())

smtpObj.quit()
