#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import os

class Modem:
    def __init__(self):
        print('Inicjuję modem.')
        self.modem = serial.Serial('/dev/ttyUSB0', 57600, timeout=5)
        time.sleep(1)

    def check_modem(self):
        if not self.modem.isOpen():
            # Jeśli z jakiś przyczyn połączenie modemu zostało przerwane zrestartuj system.
            os.system("shutdown -r now")
        else:
            print('Sprawdzenie modemu OK!')

    def write(self, command):
        self.modem.write(command)
        time.sleep(1)

    def disconnect(self):
        self.modem.close()