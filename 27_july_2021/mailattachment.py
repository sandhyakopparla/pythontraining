import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = "Sample Content"

sender_address = 'practicedigital12@gmail.com'
sender_pass = 'sandhya9@9'
receiver_address = 'sandhyakopparla24@gmail.com'

message = MIMEMultipart()
message['From'] = practicedigital12@gmail.com
message['To'] = sandhyakopparla24@gmail.com
message['Subject'] = 'A test mail sent by Python. It has an attachment.'

message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'resume_sandhya13.pdf'
attach_file = open(attach_file_name, 'rb')
# payload = MIMEBase('application', 'octate-stream')
payload = MIMEBase('application', 'pdf',Name=attach_file_name)
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 

payload.add_header('Content-Decomposition', 'attachment', filename=resume_sandhya13.pdf)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(practicedigital12@gmail.com, sandhya9@9) #login with mail_id and password
text = message.as_string()
session.sendmail(practicedigital12@gmail.com,sandhyakopparla24@gmail.com,text)
session.quit()
print('Mail Sent')