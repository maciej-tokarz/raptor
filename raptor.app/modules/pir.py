#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class Pir:
    def __init__(self):
        print('Inicjuję czujkę.')
        self.PIR_1 = 26
        # self.PIR_2 = 27
        # self.PIR_3 = 28
        # self.PIR_4 = 29
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIR_1, GPIO.IN)
        # GPIO.setup(self.PIR_2, GPIO.IN)
        # GPIO.setup(self.PIR_3, GPIO.IN)
        # GPIO.setup(self.PIR_4, GPIO.IN)
        self.status_1 = False
        # self.status_2 = False
        # self.status_3 = False
        # self.status_4 = False
        self.is_alarm = False

    def watch(self):
        i = 0
        while True:
            time.sleep(0.5)

            # Odczytaj wskazanie czujki
            self.status_1 = GPIO.input(self.PIR_1)
            # self.status_2 = GPIO.input(self.PIR_2)
            # self.status_3 = GPIO.input(self.PIR_3)
            # self.status_4 = GPIO.input(self.PIR_4)

            print('Pir 1 - status: {0}'.format(self.status_1))
            # print('Pir 2 - status: {0}'.format(self.status_2))
            # print('Pir 3 - status: {0}'.format(self.status_3))
            # print('Pir 4 - status: {0}'.format(self.status_4))

            # Jeśli czujka wykryła ruch
            # if self.status_1 or self.status_2 or self.status_3 or self.status_4 and not self.is_alarm:
            if self.status_1 and not self.is_alarm:
                i += 1
                print('Licznik ruchu: {0}'.format(i))
                # Jeśli wskazań czujki o ruchu jest więcej niż poniższy limit wszcznij alarm
                if i > 14:
                    print('Wszczynam alarm!')
                    # Wciągnij flagę alarmu
                    self.is_alarm = True
                    i = 0
            else:
                if i > 0:
                    # Jeśli czujka nie wykrywa ruchu wycofuj poziom zagrożenia
                    i -= 1
                    print('Licznik ruchu: {0}'.format(i))