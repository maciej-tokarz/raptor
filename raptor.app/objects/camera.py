#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Camera(object):
    def __init__(self, area_no, cameras_switcher, pi_camera):
        self.area_no = area_no
        self.cameras_switcher = cameras_switcher
        self.pi_camera = pi_camera

    def capture(self, path, file_name):
        self.cameras_switcher.set_camera(self.area_no)
        self.pi_camera.exif_tags['IFD0.Copyright'] = 'Raptor kamera {0}'.format(self.area_no)
        self.pi_camera.capture('{0}{1}.jpg'.format(path, file_name))
