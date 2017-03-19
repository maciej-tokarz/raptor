#!/usr/bin/env python
# -*- coding: utf-8 -*-

from objects import camera
from objects import detector


class ProtectedArea(object):
    def __init__(self, logger, area_id, detector_gpio_pin, gpio):
        self.logger = logger
        self.id = area_id
        self.camera = camera.Camera(area_id)
        self.detector = detector.Detector(detector_gpio_pin, gpio)

    def make_photo(self, path, file_name):
        try:
            if self.detector.status:
                self.camera.capture(path, file_name)
        except Exception as ex:
            self.logger.error('ProtectedArea: {0}'.format(ex))
            pass
