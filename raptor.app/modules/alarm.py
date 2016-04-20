#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from time import gmtime, strftime
import math

class Alarm:
    def __init__(self, avail_space, pir, camera, sms, email):
        print('Inicjuję alarm.')
        self.avail_space = avail_space
        self.pir = pir
        self.camera = camera
        self.sms = sms
        self.email = email
        self.alarm_started = False
        self.alarm_directory = ''
        self.alarm_name = ''
        self.alarm_photos = []

    # Monitoruj wskazania czujki.
    def watch(self):
        while True:
            time.sleep(0.5)
            if self.pir.is_alarm:
                if self.alarm_started == False:
                    print('Alarm: wszczynam alarm!')
                    self.alarm()

    def alarm(self):

        # Wciągnij flagę alarmu.
        self.alarm_started = True

        # Sprawdź dostępną przestrzeń karty pamięci
        self.avail_space.check()

        # Wyzeruj identyfikatory zdjęć z alarmu.
        self.alarm_photos = []

        # Określ właściwości alarmu.
        self.set_alarm_properties()

        # Przygotuj folder alarmu.
        self.prepare_alarm_directory()

        # Wyślij sms-a z informację o alarmie.
        self.send_sms()

        # Rozgrzej kamerę.
        self.camera.warm_camera()

        # Wykonaj serię zdjęć z alarmu.
        self.make_alarm_photos()

        # Wyślij pierwszych sześć zdjęcia z alarmu.
        self.send_six_alarm_photos()

        # Zdejmij flagi alarmu!
        print('Alarm: zdejmuję flagi alarmu.')
        self.pir.is_alarm = False
        self.alarm_started = False

    def set_alarm_properties(self):
        self.alarm_name = strftime('%Y-%m-%d %H%M', time.localtime())
        self.alarm_directory = '/home/pi/alarms/' + self.alarm_name + '/'

    def send_sms(self):
        print('Alarm: wysyłam sms-a.')
        message = 'Raptor: alarm ' + self.alarm_name
        self.sms.send('123123123', message)
        self.sms.send('234234234', message)
        
    def prepare_alarm_directory(self):
        # Przykładowa lokalizacja: /home/pi/alarms/2016-03-20 1255/
        if not os.path.exists(self.alarm_directory):
            os.makedirs(self.alarm_directory)

    def make_alarm_photos(self):
        print('Alarm: wykonuję serię zdjęć z alarmu.')
        i = 1
        while i <= 90:
            print(str(self.pir.status)) 
            if self.pir.status == True:
                photo_id = str(i).zfill(3)        
                self.camera.make_photo(self.alarm_directory, photo_id)
                self.alarm_photos.append(photo_id)
                print('Alarm: zrobiłem zdjęcie: ' + photo_id)
            time.sleep(1)
            i += 1

    def send_six_alarm_photos(self):
        print('Alarm: wysyłam pierwsze sześć zdjęć z alarmu.')
        counter = 0
        alarm_photos_len = len(self.alarm_photos)
        photos_to_send = []
        
        for i in range(0, 6, 1):
            counter += 1
            if counter > alarm_photos_len: break
            photos_to_send.append(self.alarm_directory + str(self.alarm_photos[i]) + '.jpg')
            print(self.alarm_directory + str(self.alarm_photos[i]) + '.jpg') 
        
        self.email.send_photos(
            ['foo@outlook.com', 'foo2@gmail.com'],
            'Raptor: pierwsze szesc zdjec z alarmu ' + self.alarm_name, 
            'W zalaczeniu pierwsze szesc zdjec (sposrod wykonanych ' + alarm_photos_len + ') z alarmu ' + self.alarm_name, 
            photos_to_send)