#!/usr/bin/env python
# -*- coding: utf-8 -*-

from objects import camera
from objects import detector


class ProtectedArea(object):
    def __init__(self, logger, area_no, gpio, detector_pin, cameras_switcher, pi_camera):
        self.logger = logger
        self.area_no = area_no
        self.detector = detector.Detector(gpio, detector_pin)
        self.camera = camera.Camera(area_no, cameras_switcher, pi_camera)

    def make_photo(self, path, file_name):
        try:
            if self.detector.status:
                self.camera.capture(path, file_name)
        except Exception as ex:
            self.logger.error('ProtectedArea {0} (make_photo): {1}'.format(self.area_no, ex))
            pass

    def camera_capture(self, path, file_name):
        try:
            self.camera.capture(path, file_name)
        except Exception as ex:
            self.logger.error('ProtectedArea {0} (camera_capture): {1}'.format(self.area_no, ex))
            pass

    @property
    def detector_status(self):
        return self.detector.status
