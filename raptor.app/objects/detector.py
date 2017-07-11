#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Detector(object):
    def __init__(self, gpio, detector_pin):
        print('Start Detector {0}'.format(detector_pin))
        self.gpio = gpio
        self.detector_pin = detector_pin
        gpio.setup(detector_pin, gpio.IN)

    @property
    def status(self):
        return self.gpio.input(self.detector_pin)
