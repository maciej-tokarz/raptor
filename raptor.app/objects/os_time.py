#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ntplib
from time import ctime


class OsTime:
    def __init__(self, logger):
        print('Inicjuję OsTime.')
        self.logger = logger

    def set(self):
        try:
            c = ntplib.NTPClient()
            response = c.request('europe.pool.ntp.org', version=3)
            current_time = ctime(response.tx_time)
            # current_time = 'Sun Apr 09 21:15:06 2017'
            os.system("sudo date -s '{0}'".format(current_time))
            self.logger.info('Raptor rozpoczął pracę: {0}'.format(current_time))

        except Exception as ex:
            self.logger.error('OsTime: {0}'.format(ex))
            pass
