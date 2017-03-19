#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera


class Camera(object):
    def __init__(self, area_no):
        self._area_no = area_no
        self._device = PiCamera()
        self._device.resolution = (1920, 1080)
        self._device.exif_tags['IFD0.Copyright'] = 'Raptor Camera {0}'.format(area_no)


@property
def device(self):
    return self._device
