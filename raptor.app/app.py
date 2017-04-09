#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import RPi.GPIO as gpio
import schedule
import time
from threading import Thread

sys.path.append("/home/pi/raptor.app/controllers")
sys.path.append("/home/pi/raptor.app/modules")
sys.path.append("/home/pi/raptor.app/objects")
sys.path.append("/home/pi/raptor.app/schedulers")

from picamera import PiCamera

from controllers import detectors
from controllers import avail_space
from controllers import alarm

from objects import logger
from objects import config
from objects import cameras_switcher as switcher
from objects import protected_areas as areas
from objects import modem
from objects import email_message
from objects import sms
from objects import os_time

from schedulers import photos_scheduler


class App(object):
    def __init__(self):
        self.logger = logger.Logger()
        self.config = config.Config()
        self.config.read_config()
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)
        self.cameras_switcher = switcher.CamerasSwitcher(gpio)
        self.pi_camera = PiCamera()
        self.pi_camera.resolution = (1920, 1080)
        self.protected_areas = areas.ProtectedAreas(self.logger, gpio, self.cameras_switcher, self.pi_camera)
        self.detectors_controller = detectors.Detectors(self.config, self.protected_areas)
        self.modem = modem.Modem(self.logger)
        self.email = email_message.EmailMessage(self.logger, self.config)
        self.sms = sms.Sms(self.config, self.email)
        self.avail_space_controller = avail_space.AvailSpace()
        self.alarm_controller = alarm.Alarm(
            self.logger,
            self.config,
            self.avail_space_controller,
            self.detectors_controller,
            self.protected_areas,
            self.sms,
            self.email)

    # Ustawienie czasu systemowego
    def set_os_time(self):
        os_time.OsTime(self.logger).set()

    # Uruchomienie czujek PIR
    def start_detectors(self):
        self.detectors_controller.watch()

    # Uzbrojenie alarmu
    def arming_alarm(self):
        self.alarm_controller.watch()

    # Wykonywanie zdjęć według harmonogramu
    def start_photos_scheduler(self):
        my_photos_scheduler = photos_scheduler.PhotosScheduler(
            self.logger,
            self.config,
            self.alarm_controller,
            self.protected_areas,
            self.email)
        my_photos_scheduler.start()

    def start(self):
        try:
            self.modem.check()
            self.set_os_time()

            Thread(target=self.start_detectors).start()
            Thread(target=self.arming_alarm).start()
            Thread(target=self.start_photos_scheduler).start()

            while True:
                schedule.run_pending()
                time.sleep(1)

            # Testy
            # self.sms.send('519585106', 'test')

        except Exception as ex:
            self.logger.error('Raptor: {0}'.format(ex))

app = App()
app.start()
