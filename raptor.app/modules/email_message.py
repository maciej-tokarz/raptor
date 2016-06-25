#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import smtplib
import time
from time import strftime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '


class EmailMessage:
    def __init__(self, logger, config):
        print('Inicjuję e-mail.')
        self.logger = logger
        self.config = config

    def send_photos(self, recipients=[], subject='', message='', image_paths=[]):

        try:
            multipart = MIMEMultipart()
            multipart['Subject'] = subject
            multipart['From'] = self.config.smtp_userName
            multipart['To'] = COMMASPACE.join(recipients)

            text = MIMEText(message, 'plain')
            multipart.attach(text)

            for image_path in image_paths:
                image_data = open(image_path, 'rb').read()
                multipart.attach(MIMEImage(image_data, name=os.path.basename(image_path)))

            self.send_email(recipients, multipart.as_string())

        except Exception as ex:
            self.logger.error('EmailMessage (send_photos):\n{0}'.format(ex))
            pass

    def send_email(self, recipients, message):

        try:
            self.logger.info('EmailMessage: wysyłam e-maila o {0}'.format(strftime('%Y-%m-%d %H%M', time.localtime())))
            server = smtplib.SMTP()
            server.set_debuglevel(0)
            server.connect(self.config.smtp_host, self.config.smtp_port)
            server.ehlo()
            server.starttls()
            server.login(self.config.smtp_user, self.config.smtp_password)
            server.sendmail(self.config.smtp_user, recipients, message)
            server.close()
            self.logger.info('EmailMessage: e-maila wysłany o {0}'.format(strftime('%Y-%m-%d %H%M', time.localtime())))
        except:
            self.logger.error('EmailMessage: wysłanie e-maila się nie powiodło :-(')
            pass
