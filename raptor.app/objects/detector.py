#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO


class Detector(object):
    def __init__(self, gpio_id):
        self._gpio_id = gpio_id
        GPIO.setup(gpio_id, GPIO.IN)


@property
def status(self):
    return GPIO.input(self._gpio_id)
