# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''
import smtplib
import settings
from email.mime.text import MIMEText


def sendEmail(tos, context, subject):
	
	msg = MIMEText(context,_charset = "utf-8")
	msg['Subject'] = subject
	msg['From'] = settings.email_sender
	msg['To'] = '; '.join(tos)
	#print msg.as_string()
	
	smtp = smtplib.SMTP(settings.email_server, settings.email_server_port)
	smtp.starttls()
	smtp.login(settings.email_sender_user, settings.email_sender_pwd)
	
	smtp.sendmail(settings.email_sender, tos, msg.as_string())

	smtp.quit()
	
	#print 'sended a email' + str(subject)
