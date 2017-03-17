#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser


class Config(object):
    def __init__(self):
        print('Inicjuję config.')
        self._config = ConfigParser.ConfigParser()
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
        self._config.read('raptor.cfg')
        self._recipients_phones = self._config.get('Recipients', 'phones').split(',')
        self._recipients_emails = self._config.get('Recipients', 'emails').split(',')
        self._sms_from = self._config.get('Sms', 'from')
        self._sms_email = self._config.get('Sms', 'email')
        self._sms_subject = self._config.get('Sms', 'subject')
        self._smtp_host = self._config.get('Smtp', 'host')
        self._smtp_port = self._config.get('Smtp', 'port')
        self._smtp_user = self._config.get('Smtp', 'user')
        self._smtp_username = self._config.get('Smtp', 'username')
        self._smtp_password = self._config.get('Smtp', 'password')
        self._schedulers_photo_hour = self._config.get('Schedulers', 'photo_hour')

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