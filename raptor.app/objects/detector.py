class Detector(object):
    def __init__(self, gpio_id, status, camera):
        self._gpio_id = gpio_id
        self._status = status
        self._camera = camera

@property
def gpio_id(self):
    return self._gpio_id

@property
def status(self):
    return self._status

@property
def camera(self):
    return self._camera

@status.setter
def status(self, value):
    self._status = value
