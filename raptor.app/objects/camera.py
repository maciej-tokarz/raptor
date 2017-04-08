#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Camera(object):
    def __init__(self, area_no, cameras_switcher, pi_camera):
        self._area_no = area_no
        self._cameras_switcher = cameras_switcher
        self._pi_camera = pi_camera

    def capture(self, path, file_name):
        self._cameras_switcher.set_camera(self._area_no)
        self._pi_camera.exif_tags['IFD0.Copyright'] = 'Raptor Camera {0}'.format(self._area_no)
        self._pi_camera.capture('{0}{1}.jpg'.format(path, file_name))

