#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera
import time


class Camera:
    def __init__(self, logger):
        print('Inicjuję kamerę.')
        self.logger = logger

    def make_photo(self, path, file_name):
        try:
            with PiCamera() as camera:
                camera.resolution = (1920, 1080)
                camera.exif_tags['IFD0.Copyright'] = 'Raptor'
                time.sleep(1)
                camera.capture('{0}{1}.jpg'.format(path, file_name))
        except Exception as ex:
            self.logger.error('Camera: {0}'.format(ex))
            pass
