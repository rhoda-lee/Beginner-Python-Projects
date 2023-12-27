from email.message import EmailMessage
from password import password #import password from password.py
import ssl
import smtplib


sender = "<sender email address goes here>"

#I created a separate python file called password.py and added a variable to store the password for safety reasons
sender_password = password

receipient = "<receipient email address goes here>"

subject = "Hello World!"
body = """
        Hello young human!
        Fun fact is that, I am sending this email using python code rather than an email app.
        Just a simple and fun project I am learning python with.
        Au revoir young human!
"""

em = EmailMessage()
em['From'] = sender
em['To'] = receipient
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(sender, sender_password)
    smtp.sendmail(sender, receipient, em.as_string())