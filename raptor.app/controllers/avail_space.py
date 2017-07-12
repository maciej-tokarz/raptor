#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


class AvailSpace:
    def __init__(self, logger):
        self.logger = logger

    # Sprawdź ilość dostępnego miejsca i odzyskaj jeśli potrzeba
    def check(self):
        avail_space = self.get_avail_space()
        print(str(avail_space))
        if avail_space < 500:
            self.logger.info('AvailSpace: usuwam stare alarmy.')
            self.clean_space()

    def get_avail_space(self):
        try:
            mb = 1024 * 1024
            stat = os.statvfs("/home/pi/alarms")
            return stat.f_bavail * stat.f_frsize / mb
        except Exception as ex:
            self.logger.error('AvailSpace (get_avail_space):\n{0}'.format(ex))
            pass

    def clean_space(self):
        try:
            paths = []
            for root, dirs, files in os.walk("/home/pi/alarms"):
                paths.append(root)
            paths.sort()
            paths_len = len(paths) - 1
            counter = 0
            for i in range(1, 11, 1):
                counter += 1
                if counter > paths_len:
                    break
                print(paths[i])
                shutil.rmtree(paths[i])
        except Exception as ex:
            self.logger.error('AvailSpace (clean_space):\n{0}'.format(ex))
            pass
