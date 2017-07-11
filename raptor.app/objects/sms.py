#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Sms:
    def __init__(self, config, email):
        print('Start Sms.')
        self.config = config
        self.email = email

    def send(self, recipient, message):
        try:
            body = 'from={0}&to=48{1}&raport=1&message={2}'.format(self.config.sms_from, recipient, message)
            message = '''From: {0}
To: Sms Api <sms.do@smsapi.pl>
Subject: {1}

{2}'''.format(self.config.sms_email, self.config.sms_subject, body)

            self.email.send_email(['sms.do@smsapi.pl'], message)

        except Exception as ex:
            self.logger.error('Sms (send):\n{0}'.format(ex))
            pass
