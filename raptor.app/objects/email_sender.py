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


class EmailSender:
    def __init__(self, logger, config):
        print('Start EmailSender.')
        self.logger = logger
        self.config = config
        self.server = smtplib.SMTP()

    def open_connection(self):
        try:
            start_time = strftime('%Y-%m-%d %H%M', time.localtime())
            self.logger.info('EmailSender: otwieram polaczenie z serwerem poczty o {0}'.format(start_time))
            self.server.set_debuglevel(0)
            self.server.connect(self.config.smtp_host, self.config.smtp_port)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.config.smtp_user, self.config.smtp_password)
        except Exception as ex:
            self.logger.error('EmailSender (open_connection):\n{0}'.format(ex))
            pass

    def close_connection(self):
        try:
            self.server.quit()
            end_time = strftime('%Y-%m-%d %H%M', time.localtime())
            self.logger.info('EmailSender: zamykam polaczenie z serwerem poczty o {0}'.format(end_time))
        except Exception as ex:
            self.logger.error('EmailSender (close_connection):\n{0}'.format(ex))
            pass

    def send_photos(self, recipients=[], subject='', message='', image_paths=[]):
        try:
            multipart = MIMEMultipart()
            multipart['Subject'] = subject
            multipart['From'] = self.config.smtp_username
            multipart['To'] = COMMASPACE.join(recipients)

            text = MIMEText(message, 'plain')
            multipart.attach(text)

            for image_path in image_paths:
                image_data = open(image_path, 'rb').read()
                multipart.attach(MIMEImage(image_data, name=os.path.basename(image_path)))

            self.send_email(recipients, multipart.as_string())

        except Exception as ex:
            self.logger.error('EmailSender (send_photos):\n{0}'.format(ex))
            pass

    def send_email(self, recipients, message):
        try:
            self.server.sendmail(self.config.smtp_user, recipients, message)
            time.sleep(1)
        except Exception as ex:
            self.logger.error('EmailSender (send_email):\n{0}'.format(ex))
            pass
