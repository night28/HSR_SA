"""
This script provides sending emails through a configured mailserver
"""

import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import config

def create_mail(recipient, content):
    """
    Create Mail from content with all necessary Headers

    Parameters
    ----------
    recipient (str): email address of recipient
    content (str): content of the email

    Return:
    -------
    object: an instance of mail object
    """
    date=datetime.datetime.now().date()
    msg = MIMEMultipart()
    msg['From']=config.MAIL_USER
    msg['To']=recipient
    msg['Subject']="DNA Center Report " + str(date)
    msg.attach(MIMEText(content, 'plain'))
    return msg

def send_mail(recipient, content):
    """
    Send mail to defined recipient

    Parameters
    ----------
    recipient (str): email address of recipient
    content (str): content of the email
    """
    sender = smtplib.SMTP(host=config.MAIL_SERVER, port=config.MAIL_PORT)
    sender.starttls()
    sender.login(config.MAIL_USER, config.MAIL_PASSWORD)
    sender.sendmail(config.MAIL_USER, recipient, create_mail(recipient, content).as_string())
    sender.quit()

