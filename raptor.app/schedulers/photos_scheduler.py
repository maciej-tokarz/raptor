#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import schedule
import time
from time import gmtime, strftime

class PhotosScheduler:
    def __init__(self, alarm, camera, email):
        print('Inicjuję harmonogram zdjęć.')
        self.alarm = alarm
        self.camera = camera
        self.email = email

    def start(self):

        def make_photo():
            if not self.alarm.alarm_started:
                print('PhotosScheduler: robię zdjęcie wg. harmonogramu.')
                photo_date = strftime('%Y-%m-%d %H:%M', time.localtime())
                self.camera.warm_camera()
                self.camera.make_photo('/home/pi/raptor.app/', 'photo')
                print('PhotosScheduler: wysyłam zdjęcie wg. harmonogramu.')
                self.email.send_photos(
                    ['foo@outlook.com', 'foo2@gmail.com'],
                    'Raptor: zdjecie wg. harmonogramu z dnia ' + photo_date, 
                    'W zalaczeniu zdjecie wg. harmonogramu z dnia ' + photo_date, 
                    ['/home/pi/raptor.app/photo.jpg'])
                print('PhotosScheduler: zakończyłem pracę.')
            else:
                print('PhotosScheduler: trwa alarm - zdjęcia wg. harmonogramu nie zrobię!')

        schedule.every().day.at("12:00").do(make_photo)