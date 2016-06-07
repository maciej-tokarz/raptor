#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import time


class Camera:
    def __init__(self, logger):
        print('Inicjuję kamerę.')
        self.logger = logger
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1920, 1080)
        self.camera.quality = 100
        self.camera.exif_tags['IFD0.Copyright'] = 'Raptor'

    def warm_camera(self):
        self.camera.start_preview()
        time.sleep(2)
        self.camera.stop_preview()

    def make_photo(self, path, file_name):
        try:
            file = open(path + file_name + '.jpg', 'wb')
            self.camera.capture(file)
            file.close()
        except Exception as ex:
            self.logger.error('Camera: {}'.format(ex))
            pass


