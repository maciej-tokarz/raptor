#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import smtplib
import socket
import time
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
        multipart['From'] = 'Foo'
        multipart['To'] = COMMASPACE.join(recipients)

        text = MIMEText(message, 'plain')
        multipart.attach(text)

        for image_path in image_paths:
            image_data = open(image_path, 'rb').read()
            multipart.attach(MIMEImage(image_data, name = os.path.basename(image_path)))

        self.send_email(recipients, multipart.as_string())

    def send_email(self, recipients, message):
        
        # Sprawdź modem!
        self.modem.check_modem()

        try:
            server = None
            server = self.server_connect()
            if not self.server_is_connected(server): self.server_connect(server)
            server.sendmail('foo@gmail.com', recipients, message)
            print('Wysłałem e-maila')
        except socket.error as ex:
            print('(socket.error) Nie można się połączyć z serwerem poczty:\n' + str(ex))
            pass
        except Exception as ex:
            print('Nie można się połączyć z serwerem poczty:\n' + str(ex))
            pass
        finally:
            if(server != None): self.server_disconnect(server)

    def server_connect(self):
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('foo@gmail.com', '1234')
        time.sleep(3)
        return server

    def server_is_connected(self, server):
        try:
            status = server.noop()[0]
        except:  # smtplib.SMTPServerDisconnected
            status = -1
        return True if status == 250 else False

    def server_disconnect(self, server):
        if self.server_is_connected(server): 
            server.quit()
            print('Zamknąłem połączenie z serwerem SMTP')