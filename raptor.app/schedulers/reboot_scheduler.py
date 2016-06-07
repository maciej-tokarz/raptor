#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import time
import os

class RebootScheduler:
    def __init__(self, alarm):
        print('Inicjuję harmonogram restartu.')
        self.alarm = alarm
        
    def start(self):

        def make_reboot():
            if self.alarm.alarm_started == False:
                #self.alarm.send_sms_for_reboot_test()
                os.system("shutdown -r now")
        # TODO: po testach zmienić na 05:00!
        schedule.every().monday.at("10:00").do(make_reboot)