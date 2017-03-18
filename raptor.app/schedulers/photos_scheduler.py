#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import time
from time import strftime


class PhotosScheduler:
    def __init__(self, logger, config, alarm, camera, email):
        print('Inicjuję harmonogram zdjęć.')
        self.logger = logger
        self.config = config
        self.alarm = alarm
        self.camera = camera
        self.email = email

    def start(self):
        def make_photo():
            if not self.alarm.alarm_started:
                self.logger.info('PhotosScheduler: robię zdjęcie wg. harmonogramu.')
                photo_date = strftime('%Y-%m-%d %H:%M', time.localtime())
                self.camera.warm_camera()
                self.camera.make_photo('/home/pi/raptor.app/', 'photo')
                print('PhotosScheduler: wysyłam zdjęcie wg. harmonogramu.')
                self.email.send_photos(
                    self.config.recipients_emails,
                    'Raptor: zdjecie wg. harmonogramu z dnia ' + str(photo_date),
                    'W zalaczeniu zdjecie wg. harmonogramu z dnia ' + str(photo_date),
                    ['/home/pi/raptor.app/photo.jpg'])
                self.logger.info('PhotosScheduler: zakończyłem pracę.')
            else:
                self.logger.info('PhotosScheduler: trwa alarm - zdjęcia wg. harmonogramu nie zrobię!')

        schedule.every().day.at(self.config.schedulers_photo_hour).do(make_photo)
