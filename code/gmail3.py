# Module for sending an email
import shelve
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def getCred():
    username = input('Everything before the @: ') + '@gmail.com'
    password = input('Password: ')
    shelf = shelve.open('cred_store')
    shelf['pass'] = password
    shelf['user'] = username
    shelf.close()


def sGmail(to, subject, parts):
# to is destination address
# subject is the subject line
# parts is a list of MIMEMultipart parts
    if os.path.exists('./cred_store'):
        creds = shelve.open('cred_store')
        username = creds['user']
        password = creds['pass']
        creds.close()
    else:
        getCred()
        creds = shelve.open('cred_store')
        username = creds['user']
        password = creds['pass']
        creds.close()


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = username

    # Attach parts
    for i in range(0,len(parts)):
        msg.attach(parts[i])

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(username, password)
    smtpObj.send_message(msg)
    smtpObj.quit()
