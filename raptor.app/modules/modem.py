#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: python-serial zainstalować!
import serial
import time
import os

class Modem:
    def __init__(self, logger):
        print('Inicjuję modem.')
        self.logger = logger
        self.modem = serial.Serial('/dev/ttyUSB0', 57600, timeout=5)
        time.sleep(1)

    def check_modem(self):
        if not self.modem.isOpen():
            self.logger.warn('Modem: restartuję system z powodu braku połączenia!')
            os.system("shutdown -r now")
        else:
            print('Sprawdzenie modemu OK!')

    def write(self, command):
        self.modem.write(command)
        time.sleep(1)

    def disconnect(self):
        self.modem.close()
