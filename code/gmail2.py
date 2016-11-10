# Module for sending an email
import shelve
import os
import smtplib
from email.mime.text import MIMEText


def getCred():
    username = input('Everything before the @: ') + '@gmail.com'
    password = input('Password: ')
    shelf = shelve.open('cred_store')
    shelf['pass'] = password
    shelf['user'] = username
    shelf.close()


def sGmail(to, subject, message):
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


    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = username

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(username, password)
    smtpObj.send_message(msg)
    #smtpObj.sendmail(from_addr=username, to_addrs=to, msg=message)
    smtpObj.quit()
