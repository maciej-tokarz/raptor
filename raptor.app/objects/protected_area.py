#!/usr/bin/env python
# -*- coding: utf-8 -*-

from objects import camera
from objects import detector


class ProtectedArea(object):
    def __init__(self, area_id, detector_gpio_pin):
        self._id = area_id
        self._camera = camera.Camera(area_id)
        self._detector = detector.Detector(detector_gpio_pin)


def make_area_photo(self, path, file_name):
    try:
        if self._detector.status:
            self._camera.device.capture('{0}{1}.jpg'.format(path, file_name))
            # with PiCamera() as camera:
            #     camera.resolution = self._resolution
            #     camera.exif_tags['IFD0.Copyright'] = self._copyright
            #     time.sleep(1)
            #     camera.capture('{0}{1}.jpg'.format(path, file_name))
    except Exception as ex:
        self.logger.error('Camera {0}: {1}'.format(self._area_no, ex))
        pass
