#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera


class Camera(object):
    def __init__(self, area_no):
        self._area_no = area_no
        print(area_no)
        self._device = PiCamera()
        self._device.resolution = (1920, 1080)
        self._device.exif_tags['IFD0.Copyright'] = 'Raptor Camera {0}'.format(area_no)

    def capture(self, path, file_name):
        self._device.capture('{0}{1}.jpg'.format(path, file_name))
