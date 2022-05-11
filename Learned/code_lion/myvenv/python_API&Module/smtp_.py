from email.mime import image
import imghdr
import smtplib
from email.message import EmailMessage
import re

# Simple Mail Transfer Protocol
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def send_email(addr):
    regex = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(regex,addr)):
        smtp.send_message(message)
    else:
        print("invalid address!!")

# MIME (Multipurpose Internet Mail Extensions)
message = EmailMessage()
message.set_content("codelion")

message["Subject"] = "This is Subject"
message["From"] = "lee5@gmail.com"
message["To"] = "sabin5105@gmail.com"

# rb = read binary, wb = write binary, ap = append binary
# image = open("./code_lion/myvenv/python_API&Module/macmiller.jpg","rb")
# print(image.read())

with open("./code_lion/myvenv/python_API&Module/macmiller.jpg","rb") as image:
    image_file = image.read()

# image header / identify image extention 
image_type = imghdr.what('macmiller', image_file) #.jpg
# subtype = extention
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("sabin5105@gmail.com","Aa01077112739!")

send_email("sabin5105@gmail.com")
smtp.quit()