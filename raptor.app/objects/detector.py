#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Detector(object):
    def __init__(self, gpio_id, gpio):
        self._gpio_id = gpio_id
        self._gpio = gpio
        # gpio.setup(gpio_id, gpio.IN)

    @property
    def status(self):
        return True
        # return self._gpio.input(self._gpio_id)
