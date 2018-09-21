import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender = 'sender_email-id'
receiver = 'receiver_email-id'

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = sender

# storing the receivers email address
msg['To'] = receiver

# storing the subject
msg['Subject'] = "File Trigger Required Files"

# string to store the body of the mail
body ="""Dear

Please find the attached files.

BR
Vikas
"""

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filesname = ['alu_op.txt','huawei_op.txt','nnmi_op.txt','cisco_op.txt']

for filename in filesname:
        #print(type(filename))
        attachment = open("path_to_the_file"+filename, "rb")
# instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)



server = smtplib.SMTP('smtp.outlook.com', 587)

server.starttls()

server.login('email-id', 'password')


message = msg.as_string()

server.sendmail(sender, receiver, message)

server.quit()
