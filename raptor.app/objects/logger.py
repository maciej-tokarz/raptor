#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


class Logger:
    def __init__(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%Y.%m.%d %H:%M',
            filename='raptor.log',
            filemode='a')
        self.logger = logging.getLogger('Raptor')

    def debug(self, message):
        self.logger.debug(message)
        print(message)

    def info(self, message):
        self.logger.info(message)
        print(message)

    def warn(self, message):
        self.logger.warn(message)
        print(message)

    def error(self, message):
        self.logger.error(message)
        print(message)

    def critical(self, message):
        self.logger.critical(message)
        print(message)
