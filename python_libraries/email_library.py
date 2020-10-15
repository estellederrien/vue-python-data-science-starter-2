import requests
import os, sys, time
import os.path
import re
import datetime
from datetime import date
from datetime import datetime
#from email.message import EmailMessage
import smtplib
#from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from python_config.global_variables import Global_variables
class Email_library():
    def __init__(self):
        self.tmpvar = 'temp'
    def execute(self, to_email, subject, token, email_temp):
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_address = Global_variables.fromEmailId
        from_password = Global_variables.fromEmailPassword
        to_address=to_email
        #ccEmail = 'orange@test.com, orange1@test.com'
        #ccEmail = 'add multiple ids comma separated'

        emailcontent=''
        if(email_temp=='register'):
            emailcontent=self.register_email_template(token)
        elif(email_temp=='registerv'):
            emailcontent=self.verified_email_template()
        
        mail_body = emailcontent
        
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = to_address
        #msg['Cc'] = ccEmail
        
        msg.attach(MIMEText(mail_body,'html'))

        #file = r""+file_name    # e.g. file = r"C:\Folder1\text1.txt"
        #part = MIMEBase('application', "octet-stream")
        #part.set_payload(open(file, "rb").read())
        #encoders.encode_base64(part)
        #part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
        #msg.attach(part)
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_address, from_password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
    def register_email_template(self, token):
        email_content='<div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: \'Lato\', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We\'re thrilled to have you here! Get ready to dive into your new account. </div>'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#FEF5E4" align="center">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#FEF5E4" align="center" style="padding: 0px 10px 0px 10px;">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">'
        email_content=email_content+'<h1 style="font-size: 48px; font-weight: 400; margin: 2;">Welcome!</h1> <img src="https://img.icons8.com/clouds/100/000000/handshake.png" width="125" height="120" style="display: block; border: 0px;" />'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">We\'re excited to have you get started. First, you need to confirm your account. Just press the button below.</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left">'
        email_content=email_content+'<table width="100%" border="0" cellspacing="0" cellpadding="0">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="center" style="padding: 20px 30px 60px 30px;">'
        email_content=email_content+'<table border="0" cellspacing="0" cellpadding="0">'
        email_content=email_content+'<tr>'

        email_content=email_content+'<td align="center" style="border-radius: 3px;" bgcolor="#FFA73B"><a href="'+Global_variables.websiteProductionVar+'accountconfirmation/'+token+'" target="_blank" style="font-size: 20px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #FFA73B; display: inline-block;">Confirm Account</a></td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 0px 30px 0px 30px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">If that doesn\'t work, copy and paste the following link in your browser:</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 20px 30px 20px 30px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;"><a href="#" target="_blank" style="color: #FFA73B;">'+Global_variables.websiteProductionVar+'/accountconfirmation/'+token+'/</a></p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 0px 30px 20px 30px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">If you have any questions, just reply to this email—we\'re always happy to help out.</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">Cheers,<br>solvgraph Team</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#f4f4f4" align="center" style="padding: 30px 10px 0px 10px;">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#FFECD1" align="center" style="padding: 30px 30px 30px 30px; border-radius: 4px 4px 4px 4px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<h2 style="font-size: 20px; font-weight: 400; color: #111111; margin: 0;">Need more help?</h2>'
        email_content=email_content+'<p style="margin: 0;"><a href="'+Global_variables.websiteProductionVar+'" target="_blank" style="color: #FFA73B;">We&rsquo;re here to help you out</a></p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        return email_content
    def verified_email_template(self):
        email_content='<div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: \'Lato\', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We\'re thrilled to have you here! Get ready to dive into your new account. </div>'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#FEF5E4" align="center">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#FEF5E4" align="center" style="padding: 0px 10px 0px 10px;">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">'
        email_content=email_content+'<h1 style="font-size: 48px; font-weight: 400; margin: 2;">Congrats!</h1> <img src=" https://img.icons8.com/clouds/100/000000/handshake.png" width="125" height="120" style="display: block; border: 0px;" />'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">Your solvgraph account successfully verified.</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 0px 30px 20px 30px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">If you have any questions, just reply to this email—we\'re always happy to help out.</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#ffffff" align="left" style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<p style="margin: 0;">Cheers,<br>solvgraph Team</p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#f4f4f4" align="center" style="padding: 30px 10px 0px 10px;">'
        email_content=email_content+'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">'
        email_content=email_content+'<tr>'
        email_content=email_content+'<td bgcolor="#FFECD1" align="center" style="padding: 30px 30px 30px 30px; border-radius: 4px 4px 4px 4px; color: #666666; font-family: \'Lato\', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">'
        email_content=email_content+'<h2 style="font-size: 20px; font-weight: 400; color: #111111; margin: 0;">Need more help?</h2>'
        email_content=email_content+'<p style="margin: 0;"><a href="'+Global_variables.websiteProductionVar+'" target="_blank" style="color: #FFA73B;">We&rsquo;re here to help you out</a></p>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        email_content=email_content+'</td>'
        email_content=email_content+'</tr>'
        email_content=email_content+'</table>'
        return email_content