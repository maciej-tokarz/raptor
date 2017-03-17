#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time


class Modem:
    def __init__(self, logger):
        print('Inicjuję modem.')
        self.logger = logger
        self.modem = serial.Serial('/dev/ttyUSB1', 115200, timeout=5)
        time.sleep(1)

    def check(self):
        if not self.modem.isOpen():
            self.logger.error('Modem: Brak połączenia z Internetem!')
        else:
            print('Sprawdzenie modemu OK!')

    def write(self, command):
        self.modem.write(command)
        time.sleep(1)

    def disconnect(self):
        self.modem.close()
