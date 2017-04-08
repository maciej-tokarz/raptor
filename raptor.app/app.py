#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import sys
import time
# from threading import Thread
# import schedule

sys.path.append("/home/pi/raptor.app/controllers")
sys.path.append("/home/pi/raptor.app/modules")
sys.path.append("/home/pi/raptor.app/objects")
sys.path.append("/home/pi/raptor.app/schedulers")

from picamera import PiCamera
from objects import cameras_switcher as switcher
from objects import protected_areas as areas
from controllers import detectors

# from modules import *
# zamienić poniższe:
from modules import logger
from modules import config
# from modules import os_time
# from modules import modem
# from modules import alarm
# from modules import avail_space
# from modules import camera
# from modules import email_message
# from modules import pir
# from modules import sms
# from schedulers import photos_scheduler


class App(object):
    def __init__(self):
        self.logger = logger.Logger()

        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)

        self.cameras_switcher = switcher.CamerasSwitcher(gpio)
        self.pi_camera = PiCamera()
        self.pi_camera.resolution = (1920, 1080)

        self.protected_areas = areas.ProtectedAreas(self.logger, gpio, self.cameras_switcher, self.pi_camera)
        self.config = config.Config().read_config()
        self.detectors = detectors.Detectors(self.config, self.protected_areas)

        # self.modem = modem.Modem(self.logger)
        # self.camera = camera.Camera(self.logger)
        # self.email = email_message.EmailMessage(self.logger, self.config)
        # self.sms = sms.Sms(self.config, self.email)
        # self.avail_space = avail_space.AvailSpace()
        # self.pir = pir.Pir(self.config)
        # self.alarm = alarm.Alarm(
        #     self.logger,
        #     self.config,
        #     self.avail_space,
        #     self.pir,
        #     self.camera,
        #     self.sms,
        #     self.email)

    # Ustaw czas systemowy na podstawie wzorca z Internetu
    # def set_os_time(self):
    #     os_time.OsTime(self.logger).set()

    # Uruchom moduł kontrolujący wskazania czujki/czujek ruchu
    # def start_pir(self):
    #     self.pir.watch()

    # Uruchom moduł alarmu
    # def start_alarm(self):
    #     self.alarm.watch()

    # Moduł odpowiedzialny za robienie zdjęć według harmonogramu
    # def start_photos_scheduler(self):
    #     my_photos_scheduler = photos_scheduler.PhotosScheduler(
    #         self.logger,
    #         self.config,
    #         self.alarm,
    #         self.camera,
    #         self.email)
    #     my_photos_scheduler.start()

    def start(self):
        try:
            self.detectors.watch()

            # counter = 0
            # while True:
            #     time.sleep(0.5)
            #     self.protected_areas.area_a.make_photo('/home/pi/alarms/', 'test_a_{0}'.format(counter))
            #     self.protected_areas.area_b.make_photo('/home/pi/alarms/', 'test_b_{0}'.format(counter))
            #     # area_b.make_photo('/home/pi/alarms/', 'test_b_{0}'.format(counter))
            #     print('A: {0}'.format(self.protected_areas.area_a.detector_status))
            #     print('B: {0}'.format(self.protected_areas.area_b.detector_status))
            #     counter += 1

            # Sprawdzenie modemu
            # self.modem.check()

            # Ustawienie czasu
            # self.set_os_time()

            # my_sms.send('519585106', 'test')

            # Uruchomienie składników Raptora
            # Thread(target = self.start_pir).start()
            # Thread(target = self.start_alarm).start()
            # Thread(target = self.start_photos_scheduler).start()

            # while True:
            #     schedule.run_pending()
            #     time.sleep(1)

        except Exception as ex:
            self.logger.error('Raptor: {0}'.format(ex))

app = App()
app.start()
