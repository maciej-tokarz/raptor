#!/usr/bin/env python
# -*- coding: utf-8 -*-

from objects import protected_area as area


class ProtectedAreas(object):
    def __init__(self, logger, gpio, cameras_switcher, pi_camera):
        self._area_a = area.ProtectedArea(logger, 'A', gpio, 31, cameras_switcher, pi_camera)
        self._area_b = area.ProtectedArea(logger, 'B', gpio, 33, cameras_switcher, pi_camera)
        self._area_c = area.ProtectedArea(logger, 'C', gpio, 35, cameras_switcher, pi_camera)
        self._area_d = area.ProtectedArea(logger, 'D', gpio, 37, cameras_switcher, pi_camera)

    @property
    def area_a(self):
        return self._area_a

    @property
    def area_b(self):
        return self._area_b

    @property
    def area_c(self):
        return self._area_c

    @property
    def area_d(self):
        return self._area_d
