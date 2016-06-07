#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class Pir:
    def __init__(self):
        print('Inicjuję czujkę.')
        self.PIR = 26
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIR, GPIO.IN)
        self.status = False
        self.is_alarm = False

    def watch(self):
        i = 0
        while True:
            time.sleep(1)
            # Odczytaj wskazanie czujki.
            self.status = GPIO.input(self.PIR)
            # Jeśli czujka wykryła ruch.
            if self.status:
                i += 1
                print('Pir: licznik ruchu: {0}'.format(i))
                # Jeśli wskazań czujki o ruchu jest więcej niż poniższy limit wszcznij alarm.
                if i > 5:
                    print('Pir: wszczynam alarm.')
                    # Wciągnij flagę alarmu.
                    self.is_alarm = True
                    i = 0
            else:
                # print('Pir: nie wykryto nic podejrzanego...')
                if i == 0:
                    i = 0
                else:
                    # Jeśli czujka nie wykrywa ruchu wycofuj poziom zagrożenia.
                    i -= 1
                    print('Pir: licznik ruchu: {0}'.format(i))

                    # def gpio_cleanup():
                    #    GPIO.cleanup()
