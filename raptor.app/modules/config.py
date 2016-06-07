#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser


class Config:
    def __init__(self, logger):
        print('Inicjuję config.')
        self.__logger = logger
        self.modem_pin = ''
        self.recipients_phones = ''
        self.recipients_emails = ''
        self.sms_fromSms = ''
        self.sms_fromEmail = ''
        self.sms_subject = ''
        self.smtp_host = ''
        self.smtp_port = ''
        self.smtp_user = ''
        self.smtp_userName = ''
        self.smtp_password = ''

        try:
            config = configparser.ConfigParser()
            config.read('raptor.cfg')
            self.modem_pin = config.get('Modem', 'pin')
            self.recipients_phones = config.get('Recipients', 'phones').split(',')
            self.recipients_emails = config.get('Recipients', 'emails').split(',')
            self.sms_fromSms = config.get('Sms', 'fromSms')
            self.sms_fromEmail = config.get('Sms', 'fromEmail')
            self.sms_subject = config.get('Sms', 'subject')
            self.smtp_host = config.get('Smtp', 'host')
            self.smtp_port = config.get('Smtp', 'port')
            self.smtp_user = config.get('Smtp', 'user')
            self.smtp_userName = config.get('Smtp', 'userName')
            self.smtp_password = config.get('Smtp', 'password')

        except Exception as ex:
            self.__logger.error('OsTime: ' + str(ex))
            pass

