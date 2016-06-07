#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from threading import Thread
import schedule

from modules import logger
from modules import config
from modules import os_time

# from modules import alarm
# from modules import avail_space
# from modules import camera
# from modules import email_message
# from modules import modem
# from modules import pir
# from modules import sms
# from modules import photos_scheduler
# from modules import reboot_scheduler


class App:

    global logger
    logger = logger.Logger()
    global config
    config = config.Config(logger)

    try:

        # Ustaw czas systemowy na podstawie wzorca z Internetu.
        def set_os_time(self):
            my_os_time = os_time.OsTime(self.logger)
            my_os_time.set()

        # Pobranie ustawień Raptora
        print('{}'.format(config.recipients_phones))
        print('{}'.format(config.recipients_emails))

        # Sprawdzenie modemu
        # my_modem.check_modem(__logger)

        # Ustawienie czasu
        print('OK')
        #set_os_time()

        # Testowe wywołanie restartu
        #os.system("shutdown -r now")

    except Exception as ex:
        logger.error('Raptor: {}'.format(ex))
        logger.warn('Raptor: restartuję system z powodu błędu!')
        #os.system("shutdown -r now")

        # class App:
        #     global my_log
        #     my_log = log.Log()
        #     global my_modem
        #     my_modem = modem.Modem()
        #     global my_camera
        #     my_camera = camera.Camera()
        #     global my_email
        #     my_email = email_message.EmailMessage(my_modem)
        #     global my_sms
        #     my_sms = sms.Sms(my_email)
        #     global my_avail_space
        #     my_avail_space = avail_space.AvailSpace()
        #     global my_pir
        #     my_pir = pir.Pir()
        #     global my_alarm
        #     my_alarm = alarm.Alarm(
        #         my_avail_space,
        #         my_pir,
        #         my_camera,
        #         my_sms,
        #         my_email)

        #     try:

        #         # Ustaw czas systemowy na podstawie wzorca z Internetu.
        #         def set_os_time(self):
        #             my_time = os_time.OsTime(my_log)
        #             my_time.set()

        #         # Uruchom moduł kontrolujący wskazania czujki ruchu
        #         def start_pir(self):
        #             my_pir.watch()

        #         # Uruchom moduł alarmu
        #         def start_alarm(self):
        #             my_alarm.watch()

        #         # Moduł odpowiedzialny za robienie zdjęć według harmonogramu
        #         def start_photos_scheduler(self):
        #             my_photos_scheduler = photos_scheduler.PhotosScheduler(
        #                 my_alarm,
        #                 my_camera,
        #                 my_email)
        #             my_photos_scheduler.start()

        #         # Moduł restartujący raspberry raz w tygodniu w poniedziałek o 05:00
        #         def start_reboot_scheduler(self):
        #             my_reboot_scheduler = reboot_scheduler.RebootScheduler(my_alarm)
        #             my_reboot_scheduler.start()

        #         # # # # # # # # # # # # # # # # # #
        #         # Tutaj zaczynam działanie Raptora
        #         # # # # # # # # # # # # # # # # # #

        #         # Sprawdzenie modemu
        #         my_modem.check_modem()

        #         # Ustawienie czasu
        #         set_os_time()

        #         # Uruchomienie składników Raptora
        #         Thread(target=start_pir).start()
        #         Thread(target=start_alarm).start()

        #         Thread(target=start_photos_scheduler).start()
        #         Thread(target=start_reboot_scheduler).start()

        #         while True:
        #             schedule.run_pending()
        #             time.sleep(1)

        #     except Exception as ex:
        #         print('Raptor: restartuję system z powodu błędu!')
        #         print(str(ex))
        #         my_log.writeError('Raptor', 'global', str(ex))
        #         my_log.writeMessage('Raptor: restartuję system z powodu błędu!')
        #         os.system("shutdown -r now")