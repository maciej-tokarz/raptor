#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from threading import Thread
import schedule

from modules import logger
from modules import config
from modules import os_time
from modules import modem
from modules import alarm
from modules import avail_space
from modules import camera
from modules import email_message
from modules import pir
from modules import sms
from schedulers import photos_scheduler


class App:

    global my_logger
    my_logger = logger.Logger()
    global my_config
    my_config = config.Config(my_logger)
    global my_modem
    my_modem = modem.Modem(my_logger)
    global my_camera
    my_camera = camera.Camera(my_logger)
    global my_email
    my_email = email_message.EmailMessage(my_logger, my_config, my_modem)
    global my_sms
    my_sms = sms.Sms(my_config, my_email)
    global my_avail_space
    my_avail_space = avail_space.AvailSpace()
    global my_pir
    my_pir = pir.Pir()
    global my_alarm
    my_alarm = alarm.Alarm(
        my_logger,
        my_config,
        my_avail_space,
        my_pir,
        my_camera,
        my_sms,
        my_email)

    try:

        # Ustaw czas systemowy na podstawie wzorca z Internetu.
        def set_os_time():
            my_os_time = os_time.OsTime(my_logger)
            my_os_time.set()

        # Uruchom moduł kontrolujący wskazania czujki ruchu
        def start_pir():
            my_pir.watch()

        # Uruchom moduł alarmu
        def start_alarm():
            my_alarm.watch()

        # Moduł odpowiedzialny za robienie zdjęć według harmonogramu
        def start_photos_scheduler():
            my_photos_scheduler = photos_scheduler.PhotosScheduler(
                my_logger,
                my_config,
                my_alarm,
                my_camera,
                my_email)
            my_photos_scheduler.start()

        # # # # # # # # # # # # # # # # # #
        # Tutaj zaczynam działanie Raptora
        # # # # # # # # # # # # # # # # # #

        # Sprawdzenie modemu
        my_modem.check_modem()

        # Ustawienie czasu
        set_os_time()

        # Uruchomienie składników Raptora
        Thread(target=start_pir).start()
        Thread(target=start_alarm).start()
        Thread(target=start_photos_scheduler).start()

        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as ex:
        my_logger.error('Raptor: {}'.format(ex))
        pass