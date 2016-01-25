import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import csv
import getpass
import datetime

#I know it doesn't work just yet. I'm working backwards

#user inputs
recipient = raw_input("Email address you want to send your FOIA to: ")
user = raw_input("Email username: ")
password = getpass.getpass()
name = raw_input("Your name: ")
organization = raw_input("Your organization: ")
filename = "FOIA" + str(unique_id) + ".pdf"

#connect to SMTP email server (just Outlook right now)
smtpObj = smtplib.SMTP('m.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(user, password)

#write email
to = [str(recipient)]
bcc = [user]
tos = to + bcc
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

#attach file
fileMsg = MIMEBase('application','pdf')
fileMsg.set_payload(file(str(filepath)).read())
Encoders.encode_base64(fileMsg)
fileMsg.add_header('Content-Disposition','attachment;filename=' + str(filename))
emailMsg.attach(fileMsg)

#send email and log out of SMTP server
smtpObj.sendmail(fromAddr, tos, emailMsg.as_string())
smtpObj.quit()
