#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

class EmailMessage:
    def __init__(self, modem):
        print('Inicjuję e-mail.')
        self.modem = modem

    def send_photos(self, recipients=[], subject='', message='', image_paths=[]):

        multipart = MIMEMultipart()
        multipart['Subject'] = subject
        multipart['From'] = 'foo@outlook.com'
        multipart['To'] = COMMASPACE.join(recipients)

        text = MIMEText(message, 'plain')
        multipart.attach(text)

        for image_path in image_paths:
            image_data = open(image_path, 'rb').read()
            multipart.attach(MIMEImage(image_data, name = os.path.basename(image_path)))

        self.send_email(recipients, multipart.as_string())

    def send_email(self, recipients, message):
        self.modem.check_modem()
        try:
            server = None
            server = smtplib.SMTP()
            server.connect('smtp.live.com', 587)
            server.ehlo()
            server.starttls()
            server.login('foo@outlook.com', '123123')
            server.sendmail('foo@outlook.com', recipients, message)
            print('Wysłałem e-maila')
        except socket.error as ex:
            print('Nie można się połączyć z serwerem poczty: %s' % ex)
        finally:
            if server != None:
                server.quit()