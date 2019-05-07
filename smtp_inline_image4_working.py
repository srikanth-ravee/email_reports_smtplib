import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import ssl
import secred
gmail_user = secred.gmail_user
gmail_password = secred.gmail_password

msg = MIMEMultipart('related')
msg['Subject'] = 'Internet Usage Report --Test'
msg['From'] = gmail_user
msg['To'] = secred.recipient_0
#Assign html to include inline images
html = """\
<html>
  <head></head>
    <body>
      Hello,<br><br>
      This is the report for Q1 (Jan - March '19)<br>  
      <img src="cid:image1" alt="Logo" style="width:432px;height:288px;"><br>
      <img src="cid:image2" alt="Logo" style="width:432px;height:432px;"><br>
       <br><br>
       <p>Please do not reply to this email.</p>           
    </body>
</html>
"""
# Record the MIME types of text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part2)

# This example assumes the image is in the current directory
fp = open('output1.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# For the second image
fp2 = open('output2.png', 'rb')
msgImage2 = MIMEImage(fp2.read())
fp2.close()

msgImage2.add_header('Content-ID', '<image2>')
msg.attach(msgImage2)


# Send the message via local SMTP server.
with smtplib.SMTP('smtp.gmail.com', timeout=10) as s:
    s.starttls(context=ssl.create_default_context())
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.close()
