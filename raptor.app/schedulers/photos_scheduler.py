#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import time
from time import strftime


class PhotosScheduler:
    def __init__(self, logger, config, alarm_controller, protected_areas, email):
        print('Start PhotosScheduler')
        self.logger = logger
        self.config = config
        self.alarm_controller = alarm_controller
        self.protected_areas = protected_areas
        self.email = email

    def make_photos(self):
        if not self.alarm_controller.alarm_is_started:
            self.logger.info('PhotosScheduler: robie zdjecie wg. harmonogramu.')
            photo_date = strftime('%Y-%m-%d %H:%M', time.localtime())
            photos_to_send = []

            if self.config.area_a:
                self.protected_areas.area_a.camera_capture('/home/pi/raptor.app/', 'photo_a')
                photos_to_send.append('/home/pi/raptor.app/photo_a.jpg')
            if self.config.area_b:
                self.protected_areas.area_b.camera_capture('/home/pi/raptor.app/', 'photo_b')
                photos_to_send.append('/home/pi/raptor.app/photo_b.jpg')
            if self.config.area_c:
                self.protected_areas.area_c.camera_capture('/home/pi/raptor.app/', 'photo_c')
                photos_to_send.append('/home/pi/raptor.app/photo_c.jpg')
            if self.config.area_d:
                self.protected_areas.area_d.camera_capture('/home/pi/raptor.app/', 'photo_d')
                photos_to_send.append('/home/pi/raptor.app/photo_d.jpg')

            self.email.open_connection()
            self.logger.info('PhotosScheduler: wysylam zdjecia wg. harmonogramu.')

            self.email.send_photos(
                self.config.recipients_emails,
                'Raptor: zdjecia wg. harmonogramu z dnia {0}'.format(photo_date),
                'W zalaczeniu zdjecia wg. harmonogramu z dnia {0}'.format(photo_date),
                photos_to_send)

            self.email.close_connection()
            self.logger.info('PhotosScheduler: zakonczylem prace.')
        else:
            self.logger.info('PhotosScheduler: trwa alarm - zdjec wg. harmonogramu nie wykonam!')

    def start(self):
        schedule.every().day.at(self.config.schedulers_photo_hour).do(self.make_photos)
