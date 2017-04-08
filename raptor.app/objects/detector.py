#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Detector(object):
    def __init__(self, gpio_pin, gpio):
        # self._gpio_pin = gpio_pin
        # self._gpio = gpio
        # gpio.setup(gpio_pin, gpio.IN)

    @property
    def status(self):
        return True
        # return self._gpio.input(self._gpio_pin)
