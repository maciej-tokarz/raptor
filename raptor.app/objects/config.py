#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser


class Config(object):
    def __init__(self):
        print('Inicjuję config.')
        self.config = ConfigParser.ConfigParser()
        self._area_a = False
        self._area_b = False
        self._area_c = False
        self._area_d = False
        self._recipients_phones = ''
        self._recipients_emails = ''
        self._sms_from = ''
        self._sms_email = ''
        self._sms_subject = ''
        self._smtp_host = ''
        self._smtp_port = ''
        self._smtp_user = ''
        self._smtp_username = ''
        self._smtp_password = ''
        self._schedulers_photo_hour = ''

    def read_config(self):
        self.config.read('raptor.cfg')
        self._area_a = self.config.getboolean('Areas', 'area_a')
        self._area_b = self.config.getboolean('Areas', 'area_b')
        self._area_c = self.config.getboolean('Areas', 'area_c')
        self._area_d = self.config.getboolean('Areas', 'area_d')
        self._recipients_phones = self.config.get('Recipients', 'phones').split(',')
        self._recipients_emails = self.config.get('Recipients', 'emails').split(',')
        self._sms_from = self.config.get('Sms', 'from')
        self._sms_email = self.config.get('Sms', 'email')
        self._sms_subject = self.config.get('Sms', 'subject')
        self._smtp_host = self.config.get('Smtp', 'host')
        self._smtp_port = self.config.get('Smtp', 'port')
        self._smtp_user = self.config.get('Smtp', 'user')
        self._smtp_username = self.config.get('Smtp', 'username')
        self._smtp_password = self.config.get('Smtp', 'password')
        self._schedulers_photo_hour = self.config.get('Schedulers', 'photo_hour')

    @property
    def area_a(self):
        return self._area_a

    @property
    def area_b(self):
        return self._area_b

    @property
    def area_c(self):
        return self._area_c

    @property
    def area_d(self):
        return self._area_d

    @property
    def recipients_phones(self):
        return self._recipients_phones

    @property
    def recipients_emails(self):
        return self._recipients_emails

    @property
    def sms_from(self):
        return self._sms_from

    @property
    def sms_email(self):
        return self._sms_email

    @property
    def sms_subject(self):
        return self._sms_subject

    @property
    def smtp_host(self):
        return self._smtp_host

    @property
    def smtp_port(self):
        return self._smtp_port

    @property
    def smtp_user(self):
        return self._smtp_user

    @property
    def smtp_username(self):
        return self._smtp_username

    @property
    def smtp_password(self):
        return self._smtp_password

    @property
    def schedulers_photo_hour(self):
        return self._schedulers_photo_hour
