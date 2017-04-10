#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from time import strftime


class Alarm:
    def __init__(self, logger, config, avail_space_controller, detectors_controller, protected_areas, sms, email):
        print('Inicjuję alarm.')
        self.logger = logger
        self.config = config
        self.avail_space_controller = avail_space_controller
        self.detectors_controller = detectors_controller
        self.protected_areas = protected_areas
        self.sms = sms
        self.email = email
        self._alarm_is_started = False
        self.alarm_directory = ''
        self.alarm_name = ''
        self.alarm_photos = []

    @property
    def alarm_is_started(self):
        return self._alarm_is_started

    # Monitoruj wskazania czujek
    def arming_alarm(self):
        while True:
            time.sleep(0.5)
            if self.detectors_controller.is_alarm:
                if not self._alarm_is_started:
                    self.logger.info('Alarm: wszczynam alarm!')
                    self.start_alarm()

    def start_alarm(self):

        # Wciągnij flagę alarmu
        self._alarm_is_started = True

        # Sprawdź dostępną przestrzeń karty pamięci
        self.avail_space_controller.check()

        # Wyzeruj identyfikatory zdjęć z poprzedniego alarmu
        self.alarm_photos = []

        # Określ właściwości alarmu
        self.set_alarm_properties()

        # Przygotuj folder alarmu.
        self.prepare_alarm_directory()

        # Wykonaj serię zdjęć z alarmu
        self.make_alarm_photos()

        # Wyślij sms-a z informację o alarmie
        self.send_sms()

        # Wyślij pierwszych sześć zdjęć z alarmu
        self.send_six_alarm_photos()

        # Zdejmij flagę alarmu!
        self.remove_alarm_flag()

    def set_alarm_properties(self):
        self.alarm_name = strftime('%Y-%m-%d %H%M', time.localtime())
        self.alarm_directory = '/home/pi/alarms/{0}/'.format(self.alarm_name)

    def prepare_alarm_directory(self):
        # Przykładowa lokalizacja: /home/pi/alarms/2016-03-20 1255/
        if not os.path.exists(self.alarm_directory):
            os.makedirs(self.alarm_directory)

    def make_alarm_photos(self):
        print('Alarm: wykonuję serię zdjęć z alarmu.')
        i = 1
        while i <= 60:
            photo_id = str(i).zfill(3)
            if self.config.area_a:
                file_name_a = '{0}_a'.format(photo_id)
                self.protected_areas_controller.area_a.make_photo(self.alarm_directory, file_name_a)
                self.alarm_photos.append(file_name_a)
            if self.config.area_b:
                file_name_b = '{0}_b'.format(photo_id)
                self.protected_areas_controller.area_b.make_photo(self.alarm_directory, file_name_b)
                self.alarm_photos.append(file_name_b)
            if self.config.area_c:
                file_name_c = '{0}_c'.format(photo_id)
                self.protected_areas_controller.area_c.make_photo(self.alarm_directory, file_name_c)
                self.alarm_photos.append(file_name_c)
            if self.config.area_d:
                file_name_d = '{0}_d'.format(photo_id)
                self.protected_areas_controller.area_d.make_photo(self.alarm_directory, file_name_d)
                self.alarm_photos.append(file_name_d)
            time.sleep(1)
            i += 1

    def send_sms(self):
        message = 'Raptor: alarm {0}'.format(self.alarm_name)
        for phone in self.config.recipients_phones:
            self.sms.send(phone, message)

    def send_six_alarm_photos(self):
        print('Alarm: wysyłam pierwsze sześć zdjęć z alarmu.')
        counter = 0
        alarm_photos_len = len(self.alarm_photos)
        photos_to_send = []

        for i in range(0, 6, 1):
            counter += 1
            if counter > alarm_photos_len:
                break
            photo_path = '{0}{1}.jpg'.format(self.alarm_directory, self.alarm_photos[i])
            photos_to_send.append(photo_path)

        self.email.send_photos(
            self.config.recipients_emails,
            'Raptor: pierwsze szesc zdjec z alarmu {0}'.format(self.alarm_name),
            'W zalaczeniu pierwsze szesc zdjec (sposrod wykonanych {0}) z alarmu {1}'.format(
                alarm_photos_len,
                self.alarm_name),
            photos_to_send)

    def remove_alarm_flag(self):
        self.logger.info('Alarm: zdejmuję flagi alarmu.')
        self.detectors_controller.is_alarm = False
        self._alarm_is_started = False
