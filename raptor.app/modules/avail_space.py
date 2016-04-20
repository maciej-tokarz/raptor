#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

class AvailSpace:

    # Sprawdź ilość dostępnego miejsca i odzyskaj jeśli potrzeba.
    def check(self):
        avail_space = self.get_avail_space()
        print(str(avail_space))
        if avail_space < 500:
            self.clean_space()

    def get_avail_space(self):
        mb = 1024 * 1024
        stat = os.statvfs("/home/pi/alarms")
        return stat.f_bavail * stat.f_frsize / mb

    def clean_space(self):
        paths = []
        for root, dirs, files in os.walk("/home/pi/alarms"):
            paths.append(root)
        paths.sort()
        paths_len = len(paths) - 1
        counter = 0
        for i in range(1, 11, 1):
            counter += 1
            if counter > paths_len: break
            print(paths[i])
            shutil.rmtree(paths[i])