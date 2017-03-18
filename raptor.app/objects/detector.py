class Detector(object):
    def __init__(self, gpio_id, status):
        self._gpio_id = gpio_id
        self._status = status

@property
def gpio_id(self):
    return self._gpio_id

@property
def status(self):
    return self._status

@status.setter
def status(self, value):
    self._status = value
