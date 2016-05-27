#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntplib
import time
import os

class OsTime:

    def set(self):
        try:
            client = ntplib.NTPClient()
            response = client.request('pool.ntp.org')
            utc_time = response.tx_time
            os.system("sudo date -s '" + str(time.ctime(utc_time)) + "'")
            print ('Ustawiłem aktualny czas: ' + str(time.ctime(utc_time)))
        except Exception as ex:
            print(str(ex))
            print ('Nie ustawiłem daty i czasu.')
            pass