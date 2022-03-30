import smtplib
from email.message import EmailMessage
import getpass

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email, password)
from_address = email
to_address = email
subject = input("Subject: ")
message = input("Body Message: :")
msg = "Subject: "+subject+'\n'+message
smtp_object.sendmail(from_address, to_address, msg)
