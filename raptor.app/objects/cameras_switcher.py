#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CamerasSwitcher(object):
    def __init__(self, gpio):
        self._gpio = gpio
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(12, gpio.OUT)

    def set_camera(self, area_no):
        if area_no == 'A':
            self._gpio.output(7, False)
            self._gpio.output(11, False)
            self._gpio.output(12, True)
        if area_no == 'B':
            self._gpio.output(7, True)
            self._gpio.output(11, False)
            self._gpio.output(12, True)
        if area_no == 'C':
            self._gpio.output(7, False)
            self._gpio.output(11, True)
            self._gpio.output(12, False)
        if area_no == 'D':
            self._gpio.output(7, True)
            self._gpio.output(11, True)
            self._gpio.output(12, False)
