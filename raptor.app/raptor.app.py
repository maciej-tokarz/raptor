#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from threading import Thread
import schedule
import time
import os
import sys  

from modules import alarm
from modules import camera
from modules import email_message
from modules import avail_space
from modules import modem
from modules import os_time
from modules import pir
from modules import sms

from schedulers import photos_scheduler
from schedulers import reboot_scheduler

class Raptor:
    global my_modem
    my_modem = modem.Modem()
    global my_camera
    my_camera = camera.Camera()
    global my_email
    my_email = email_message.EmailMessage(my_modem)
    global my_sms
    my_sms = sms.Sms(my_email)
    global my_avail_space
    my_avail_space = avail_space.AvailSpace()
    global my_pir
    my_pir = pir.Pir()
    global my_alarm
    my_alarm = alarm.Alarm(
        my_avail_space, 
        my_pir, 
        my_camera, 
        my_sms, 
        my_email)

    try:

        # Uruchom modem.
        def start_modem():
            my_modem.connect()

        # Ustaw czas systemowy na podstawie wzorca z Internetu.
        def set_os_time():
            my_time = os_time.OsTime()
            my_time.set()
            
        # Uruchom moduł kontrolujący wskazania czujki ruchu
        def start_pir():
            my_pir.watch()

        # Uruchom moduł alarmu
        def start_alarm():
            my_alarm.watch()
            
        # Moduł odpowiedzialny za robienie zdjęć według harmonogramu
        def start_photos_scheduler():
            my_photos_scheduler = photos_scheduler.PhotosScheduler(
                my_alarm, 
                my_camera, 
                my_email)
            my_photos_scheduler.start()

        # Moduł restartujący raspberry raz w tygodniu w poniedziałek o 05:00
        def start_reboot_scheduler():
            my_reboot_scheduler = reboot_scheduler.RebootScheduler(my_alarm)
            my_reboot_scheduler.start()
        
        # Uruchomienie składników Raptora
        Thread(target = start_modem).start()
        set_os_time()

        Thread(target = start_pir).start()
        Thread(target = start_alarm).start()
        
        Thread(target = start_photos_scheduler).start()
        Thread(target = start_reboot_scheduler).start()

        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        my_pir.gpio_cleanup

    except Exception as ex: 
        print(str(ex))
        print('Raptor: restartuję system z powodu błędu!')
        os.system("shutdown -r now")