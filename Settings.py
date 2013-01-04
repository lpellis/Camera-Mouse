'''
Created on Oct 17, 2012

@author: Loftie Ellis
'''

import VideoCapture
import cv2
import json
import copy

class Settings:

    def __init__(self, parent):
        self.parent = parent
        self.defaults = {'face_tracking':
                            {'camera_id' : 0, 'speed': 50},
                            'blob': 2
                        }
        self.settings = {}
        self.camera_list = []
        self._camera_list = []
        self.face_tracking_camera = None
        self._face_tracking_camera_id = None

        try:
            s = open('options.json').read()
            self.settings = json.loads(s)
        except:
            json.dump(self.defaults, open('options.json', 'w'), sort_keys=True, indent=True)

        #merge the default settings with the loaded settings
        for k, v in self.defaults.iteritems():
            if not k in self.settings:
                self.settings[k] = v
            if type(v) is dict:
                for k2, v2 in v.iteritems():
                    if not k2 in self.settings[k]:
                        self.settings[k][k2] = v2

        self.defaults = copy.deepcopy(self.settings)
        self.load_camera_list()
        self.apply_settings()


    def apply_settings(self, settings=None):
        if (settings):
            self.settings = copy.deepcopy(settings)
        self.load_face_tracking_camera(self.settings['face_tracking']['camera_id'])

    def load_face_tracking_camera(self, camera_id):

        print 'loading camera: ', camera_id
        if (camera_id == self._face_tracking_camera_id):
            print 'skipping'
            return

        if camera_id > len(self.camera_list):
            camera_id = 0
        self.settings['face_tracking']['camera_id'] = camera_id

        try:
            self.face_tracking_camera.release()
            del(self.face_tracking_camera)
            del(self.parent.camera)
        except:
            pass
        self.face_tracking_camera = cv2.VideoCapture(self.settings['face_tracking']['camera_id'])
        self.parent.camera = self.face_tracking_camera
        self._face_tracking_camera_id = camera_id

    def save(self):
        self.defaults = copy.deepcopy(self.settings)
        json.dump(self.settings, open('options.json', 'w'), sort_keys=True, indent=True)

    def load_camera_list(self):
        i = 0

        while i < 2:
            try:
                c = VideoCapture.Device(i)
                self.camera_list.append({'name': c.getDisplayName(), 'device': c})
                i += 1
            except:
                break

        if len(self.camera_list) == 0:
            return

#        self.camera_main = self.camera_list[0]['device']


if __name__ == "__main__":
    settings = Settings()
