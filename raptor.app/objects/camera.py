class Camera(object):
    def __init__(self, id, detector):
        self._id = id
        self._resolution = (1920, 1080)
        self._copyright = 'Raptor Cam {0}'.format(id)
        self._detector = detector

@property
def id(self):
    return self._id

def make_photo(self, path, file_name):
    try:
        if self._detector.status:
            with PiCamera() as camera:
                camera.resolution = self._resolution
                camera.exif_tags['IFD0.Copyright'] = self._copyright
                time.sleep(1)
                camera.capture('{0}{1}.jpg'.format(path, file_name))
    except Exception as ex:
        self.logger.error('Camera: {0}'.format(ex))
        pass
