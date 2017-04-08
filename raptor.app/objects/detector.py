#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Detector(object):
    def __init__(self, gpio, detector_pin):
        self._gpio = gpio
        self._detector_pin = detector_pin
        gpio.setup(detector_pin, gpio.IN)

    @property
    def status(self):
        return self._gpio.input(self._detector_pin)
