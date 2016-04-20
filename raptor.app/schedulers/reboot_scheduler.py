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
                os.system("shutdown -r now")

        schedule.every().monday.at("05:00").do(make_reboot)