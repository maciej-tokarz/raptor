#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import os

class Modem:
    def __init__(self):
        print('Inicjuję modem.')
        self.modem = serial.Serial('/dev/ttyUSB0', 115200, timeout=5)
        time.sleep(1)
        # ATE - włącz echo interfejsu szeregowego. 
        self.write('ATE1\r')
        # AT+CPIN - wprowadź kod PIN. 
        self.write('AT+CPIN=8577\r')

    def connect(self):
        # Połącz z Internetem.
        self.write('AT+CGDCONT=1,"IP","internet"\r')
        self.write('ATD*99#\r')

    def check_modem(self):
        if not self.modem.isOpen():
            # Jeśli z jakiś przyczyn połączenie modemu zostało przerwane zrestartuj system.
            os.system("shutdown -r now")

    def write(self, command):
        self.modem.write(command)
        time.sleep(1)

    def disconnect(self):
        self.modem.close()