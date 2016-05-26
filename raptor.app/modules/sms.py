#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Sms:
    def __init__(self, email):
        print('Inicjuję sms.')
        self.email = email

    def send(self, recipient, message):
        body = 'from=SMSAPI!&to=48' + recipient + '&raport=1&message=' + message
        my_message = '''From: Foo <foo@gmail.com>
To: Sms Api <sms.do@smsapi.pl>
Subject: login@8456fkty567gb3bg37b357b3457b3457

{}'''.format(body)
        print(my_message)
        self.email.send_email(
            ['sms.do@smsapi.pl'],
            my_message)