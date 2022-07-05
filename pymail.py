from distutils.log import error
import smtplib
import sys
import os
import json

configfile=open("pymail.json", "r")
config=json.load(configfile)

strgg=config["error_strings"]
mailsto=config["mailsto"]

from email import encoders

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
def checkstr(str, strg):
    for s in strg:
        if s in str:
            return True
    return False

attfile=sys.argv[1]
attfilef=open(attfile,"r")
logcontent=attfilef.read()
errorlines=logcontent.split("\n")
errorlines=[a for a in errorlines if checkstr(a,strgg)]
errorlines="\n".join(errorlines)
if checkstr(logcontent, strgg)>-1:
    print("Attachment file: " + attfile)
    msg = MIMEMultipart()
    msg['Subject'] = config["mailsubject"] 
    msg['From'] = config["mailfrom"]
    msg['To'] = ', '.join(mailsto)
    msg.attach(MIMEText(config["mailtext"]+":\n" + errorlines))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(attfile, "rb").read())
    encoders.encode_base64(part)
        
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attfile));

    msg.attach(part)

    password = config["mailpwd"]
    mailserver = smtplib.SMTP(config["mailserver"], 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(config["maillogin"], password)
    mailserver.sendmail(config["maillogin"], ', '.join(mailsto), msg.as_string())
    mailserver.quit()

attfilef.close()