#encoding: utf-8
'''
Created on 2013-7-1

@author: fengxuefeng
'''

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pt_config import config_util
import mimetypes
import smtplib
import sys
import traceback
from smtplib import SMTPException

host = config_util.Config().get("email", "email_host")
user = config_util.Config().get("email", "email_user")
password = config_util.Config().get("email", "email_password")

def send_mime_email(email_from, email_to, subject, message, attached_file, attached_name, is_html_message = False):
    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = ", ".join(email_to)
    msg["Subject"] = subject
    
    # 邮件内容
    text_type = "plain"
    if is_html_message:
        text_type = "html"
    text = MIMEText(message, text_type, "utf-8")
    msg.attach(text)
    
    # 附件
    i = 0
    for file in attached_file:
        file_name = attached_name[i]
        i = i + 1
        
        ctype, encoding = mimetypes.guess_type(file) 
        if ctype is None or encoding is not None:     
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        att = MIMEImage((lambda f: (f.read(), f.close()))(open(file, 'rb'))[0], _subtype = subtype) 
        att.add_header('Content-Disposition', 'attachment', filename = file_name) 
        msg.attach(att)
        
    try:
        smtp = smtplib.SMTP(host)
        smtp.login(user, password)
        smtp.sendmail(email_from, email_to, msg.as_string())
        smtp.quit()
    except SMTPException:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        traceback.print_exception(exceptionType, exceptionValue, exceptionTraceback, limit = 2, file = sys.stdout)
        print "Error: unable to send email"