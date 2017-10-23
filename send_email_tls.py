#Python script to send email securely using SMTP and TLS
#getpass module allows us to ask user for password input

import getpass
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#we specify our mail server
SMTP_SERVER = 'smtp.gmail.com'
#for the port we give the default TLS port 587. SSL is 465
SMTP_PORT = 587

#define method to send secure email
def send_email(sender, recipient):
    """Send Email"""
    #Ensures that we send our message as HTML/Text
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    msg['Subject'] = input("Please Enter a Subject For Your Email: ")
    message = input("Please Type in Your Message Here. Press Enter to Continue when you are Done: ")
#   #Handles plaintext versions of our message
    part = MIMEText('text', "plain")
    msg.attach = part

    #open the SMTP session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #Add debugger to display any errors
    session.set_debuglevel(1)
    #Establishes a proper SMTP session with the mail server
    session.ehlo()
    #start our TLS session
    session.starttls()
    session.ehlo()
    password = getpass.getpass(prompt="Enter your Email Password: ")
    #if password is successful, login to session
    session.login(sender, password)
    #send the email after successful login
    session.sendmail(sender, recipient, msg.as_string())
    print("Email sent successfully to {0}.".format(recipient))
    session.quit()

if __name__ == "__main__":
    sender = input("Enter the sender's email address: ")
    recipient = input("Enter the recipeint's email address: ")
    send_email(sender, recipient)
