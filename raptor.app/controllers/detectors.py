#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class Detectors(object):
    def __init__(self, config, protected_areas):
        print('Start Detectors.')
        self.config = config
        self.protected_areas = protected_areas
        self.detector_status_a = False
        self.detector_status_b = False
        self.detector_status_c = False
        self.detector_status_d = False
        self._is_alarm = False

    @property
    def is_alarm(self):
        return self._is_alarm

    @is_alarm.setter
    def is_alarm(self, value):
        self._is_alarm = value

    def track_detectors(self):
        i = 0
        while True:
            time.sleep(0.5)

            # Odczytaj wskazanie czujek
            self.detector_status_a = self.protected_areas.area_a.detector_status
            self.detector_status_b = self.protected_areas.area_b.detector_status
            self.detector_status_c = self.protected_areas.area_c.detector_status
            self.detector_status_d = self.protected_areas.area_d.detector_status

            # print('Detector A: {0}'.format(self.detector_status_a))
            # print('Detector B: {0}'.format(self.detector_status_b))
            # print('Detector C: {0}'.format(self.detector_status_c))
            # print('Detector D: {0}'.format(self.detector_status_d))

            # Jeśli czujka wykryła ruch
            if self.detector_status_a or \
                    self.detector_status_b or \
                    self.detector_status_c or \
                    self.detector_status_d and not \
                    self.is_alarm:

                i += 1
                # print('Licznik ruchu: {0}'.format(i))
                # Jeśli wskazań czujki jest więcej niż poniższy limit wszcznij alarm
                if i > 15:
                    print('Wszczynam alarm!')
                    # Wciągnij flagę alarmu
                    self._is_alarm = True
                    i = 0
            else:
                if i > 0:
                    # Jeśli czujka nie wykrywa ruchu wycofuj poziom zagrożenia
                    i -= 1
                    # print('Licznik ruchu: {0}'.format(i))
