import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import time
#import pytz

t2= time.time()
t = "1609459200"
t1= int(t2)-int(t)

pythonanywhereaccount="Specify the function number and module name as in logic file"

date = datetime.datetime.now().date()
curr_time = time.localtime()
time = time.strftime("%H:%M:%S", curr_time)

fromaddr = "testdowell123@gmail.com"
toaddr = ["thomas@dowellresearch.sg","manish@dowellresearch.in","charumaheshwari41@gmail.com","anjanas@dowellresearch.in"]
#toaddr = ["manish@dowellresearch.in"]
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)

msg['Subject'] = "libary with thier licenses"
body = f"The text file of libaries and licenses used in {pythonanywhereaccount} module !"

os.system("pip install pip-licenses")
#filename

userinput = f"license{t1}.txt"

#run command
os.system(f"pip-licenses > {userinput}")

#mail
msg.attach(MIMEText(body, 'plain'))
filename = userinput
attachment = open(userinput, "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "jplsyqzgpdvzuwda")
text = msg.as_string()
s.sendmail(fromaddr, toaddr,text)
s.quit()
os.remove(userinput)
