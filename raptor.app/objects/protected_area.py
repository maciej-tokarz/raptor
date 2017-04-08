#!/usr/bin/env python
# -*- coding: utf-8 -*-

from objects import camera
# from objects import detector

class ProtectedArea(object):
    def __init__(self, logger, area_no, detector_gpio_pin, gpio, cameras_switcher, pi_camera):
        self.logger = logger
        self._area_no = area_no
        self._cameras_switcher = cameras_switcher
        self._camera = camera.Camera(area_no, cameras_switcher, pi_camera)
        # self.detector = detector.Detector(detector_gpio_pin, gpio)

    def make_photo(self, path, file_name):
        try:
            self._camera.capture(path, file_name)
            # if self.detector.status:
            #     self._camera.capture(path, file_name)
        except Exception as ex:
            self.logger.error('ProtectedArea: {0}'.format(ex))
            pass
