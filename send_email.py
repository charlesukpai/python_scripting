#Simple python email script. Sends email using only SMTP
#We use python's inbuilt SMTP library
#We also use MIME(Mulit-purpose internet mail extensions)

import smtplib
#Allows us send an email with images
from email.mime.image import MIMEImage
#Mumltipart allows our email to be sent as either HTML or Text or both
from email.mime.multipart import MIMEMultipart
#Allows us to wrap a plaintext message
from email.mime.text import MIMEText

#we set our mail server. Cna be any mail server. Yahoo, Google (smtp.gmail.com) e.t.c
SMTP_SERVER = input("Enter preffered mail server here: ")
#Specify the SMTP port. We can use the default or use 587(TLS), 465 (SSL)
SMTP_PORT = 25

#define the send email method taking 2 arguements sender and recipient
def send_email(sender, recipient):
    """Send Email Message"""
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender

    #We ask the user to type in the email subject and the body of the message
    subject = input("Enter Email Subject Here: ")
    msg['Subject'] = subject
    message = input("Enter your message here. Press Enter to Continue: ")
    #wrap a plain-text message  passing it two argeuments
    part = MIMEText('text', "plain")
    #set data in our email
    part.set_payload(message)
    msg.attach(part)
    #start our SMTP session specifying the mail server and port to use
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #Establishes a proper SMTP session with the mail server
    session.ehlo()
    #send our email
    session.sendmail(sender, recipient, msg.as_string())
    print("Email sent successfully to {0}.".format(recipient))
    #Close session after sending email
    session.quit()

if __name__ == '__main__':
    sender = input("Enter an Email Address for the Sender: ")
    recipient = input("Enter an Email Address for the Recipient: ")
    send_email(sender, recipient)
