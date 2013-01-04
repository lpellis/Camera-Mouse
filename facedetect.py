from __future__ import division
import numpy as np

import cv2
import cv2.cv as cv
#from video import create_capture
from ltools.common import clock, draw_str
from ltools import tracker
import ltools.geometry

class FaceDetect:

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")
#        self.eye_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_mcs_righteye.xml")
        self.eye_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
        self.nose_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_mcs_nose.xml")
        self._face_history = []
        self._HISTORY_LEN = 30   #used to compute the running avg of face size
        self.face_rect = []
        self._MEDIAN_LEN = 10
        self._nose_history = []
        self._nose_pos_list = []
        self.nose_rect = []
        self.zero_pos = []

        self.tracker = tracker.LKTracker()
        self.tracker.display_window = 1
        self.ready = 0
        self._ready_count = 0
        self._tracker_offset = [0, 0]
        self.tempval = []
        self._diffsize = 0

    def log_face_rect(self, face_rect):
        if not len(face_rect):
            return
        self._face_history.insert(0, face_rect)
        if len(self._face_history) > self._HISTORY_LEN:
            self._face_history.pop()

    def log_nose_rect(self, nose_rect):
        if not len(nose_rect):
            return
        self._nose_history.insert(0, nose_rect)
        if len(self._nose_history) > self._HISTORY_LEN:
            self._nose_history.pop()

    def update(self, color_img):

        if self.ready:
            self.tracker.update(color_img)
#            self.update_positions_using_tracker()

            x1, y1, w, h = self.face_rect
            t1, t2, w, h = np.int32(np.median(self._face_history, axis=0))
            c = self.tracker.get_center() - self._tracker_offset
            self.face_rect = np.array([max(0, c[0] - (w // 2)), max(0, c[1] - (h // 2)), w, h])
#            print self.face_rect_raw - self.tempval
            x1r, y1r, wr, hr = self.face_rect_raw
            diff = np.array([x1r + (wr // 2), y1r + (hr // 2)]) - self.zero_pos
            self._diffsize = np.sum(np.abs(diff)) / w
#            print self._diffsize

        grayscale_img = ltools.image.convert_to_grayscale(color_img)
        face_rect_raw = self.detect_face_with_cascade(grayscale_img)


        if not len(face_rect_raw):
            return

        self.face_rect_raw = face_rect_raw

        log_sizes = (not self.ready) or (self.ready and self._diffsize < 0.1)
        if log_sizes:
            self.log_face_rect(face_rect_raw)

            if not self.ready:  #if lktracking has not yet begun then we just use avg, assume user looks directly at camera
                self.face_rect = np.int32(np.median(self._face_history, axis=0))

            x1, y1, w, h = self.face_rect
            face_img = grayscale_img[y1:y1 + h, x1:x1 + w]

            self.log_nose_rect(self.detect_nose_with_cascade(face_img))

            if not self.ready:
                self._ready_count += 1
                if self._ready_count == 10:
                    self.ready = 1
                    self.zero_pos = np.array([x1 + (w // 2), y1 + (h // 2)])

                    if not len(self._nose_history):
                        self.nose_rect = np.int32([w / 3, w / 2, w / 2.3, w / 2.8])
                    else:
                        self.nose_rect = np.int32(np.median(self._nose_history, axis=0))

                    self.tracker.update(color_img)

                    n_x, n_y, n_w, n_h = self.nose_rect
                    self._tracker_offset = np.array([n_x + (n_w // 2) - (w // 2), n_y + (n_h // 2) - (h // 2)])
                    self.tracker.reset([self.nose_rect[0] + self.face_rect[0], self.nose_rect[1] + self.face_rect[1], self.nose_rect[2], self.nose_rect[3]])


            else:
                d = ltools.geometry.rect_center(self.face_rect) - ltools.geometry.rect_center(self.face_rect_raw)
                d = np.sum(np.abs(d)) / w
#                print d
                if d > 0.15:
                    self.tracker.reset([self.nose_rect[0] + self.face_rect_raw[0], self.nose_rect[1] + self.face_rect_raw[1], self.nose_rect[2], self.nose_rect[3]])
                    print 'XXXXX'


                pass
            return
        return

        x1, y1, x2, y2 = self.face_rect
        w = x2 - x1
        h = y2 - y1
        self.tracker.reset([x1 + w // 3 , y1 + w // 3 + (w // 8) , w // 3 , w // 3 ])

    def update_zero_pos(self, zero_pos):
        self.zero_pos = zero_pos

    def detect_nose_with_cascade(self, img):

        rects = self.nose_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10), flags=cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) == 0:
            if not len(self.nose_rect):
                h, w = img.shape
                self.nose_rect = np.array([w // 3, h // 3, (w // 3) * 2, (h // 3) * 2])

            return []

#        rects[:, 2:] += rects[:, :2]  #transforsms [x, y, w, h] to [x, y, x+w, y+h]
        return rects[0]

        rect = rects[0]  #just choose the first XXX choose biggest here

        self._nose_sizes_list.insert(0, rect)
        self._nose_pos_list.insert(0, rect)
        if len(self._nose_sizes_list) > self._MEDIAN_LEN:
            self._nose_sizes_list.pop()
            self._nose_pos_list.pop()

        s_w, s_h = 0, 0
        s_l, s_t = 0, 0
        for r in self._nose_sizes_list:
            s_w += r[2] - r[0]
            s_h += r[3] - r[1]
            s_l += r[0]
            s_t += r[1]

        w, h = s_w / len(self._nose_sizes_list), s_h / len(self._nose_sizes_list)
        l, t = s_l / len(self._nose_sizes_list), s_t / len(self._nose_sizes_list)
        x1, y1, x2, y2 = rect

        self.nose_rect = np.array([int(t) for t in [l, t, l + w, t + h ]])

    def detect_eyes_with_cascade(self, img):

        rects = self.eye_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10), flags=cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) == 0:
            return []

        rects[:, 2:] += rects[:, :2]  #transforsms [x, y, w, h] to [x, y, x+w, y+h]
        return rects
        rect = rects[0]  #just choose the first face XXX choose biggest here




        self._face_sizes_list.insert(0, rect)
        if len(self._face_sizes_list) > self._HISTORY_LEN:
            self._face_sizes_list.pop()

        s_w, s_h = 0, 0
        for r in self._face_sizes_list:
            s_w += r[2] - r[0]
            s_h += r[3] - r[1]

        w, h = s_w / len(self._face_sizes_list), s_h / len(self._face_sizes_list)
        x1, y1, x2, y2 = rect

        self.face_rect = [int(t) for t in [x1, y1, x1 + w, y1 + h ]]

    def detect_face_with_cascade(self, img):
        rects = self.face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags=cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) == 0:
            return []

#        rects[:, 2:] += rects[:, :2]  #transforsms [x, y, w, h] to [x, y, x+w, y+h]
        rect = rects[0]  #just choose the first face XXX choose biggest here

        return rects[0]  #just choose the first face XXX choose biggest here

        if (not self.zero_pos):
            x1, y1, x2, y2 = rect
            w = x2 - x1
            h = y2 - y1
            self.update_zero_pos([x1 + (w // 2), y1 + (h // 2)])

        self._face_sizes_list.insert(0, rect)
        if len(self._face_sizes_list) > self._HISTORY_LEN:
            self._face_sizes_list.pop()

        s_w, s_h = 0, 0
        for r in self._face_sizes_list:
            s_w += r[2] - r[0]
            s_h += r[3] - r[1]

        w, h = s_w / len(self._face_sizes_list), s_h / len(self._face_sizes_list)
        x1, y1, x2, y2 = rect

        self.face_rect = [int(t) for t in [x1, y1, x1 + w, y1 + h ]]


if __name__ == '__main__':
    import sys, getopt
    print help_message

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 'synth:bg=../cpp/lena.jpg:noise=0.05'

    video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "../../../data/haarcascades/haarcascade_frontalface_default.xml")
    nested_fn = args.get('--nested-cascade', "../../../data/haarcascades/haarcascade_mcs_lefteye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = create_capture(video_src)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            vis_roi = vis[y1:y2, x1:x2]
            subrects = detect(roi.copy(), nested)
            draw_rects(vis_roi, subrects, (255, 0, 0))
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt * 1000))
        cv2.imshow('facedetect', vis)

        if cv2.waitKey(5) == 27:
            break

