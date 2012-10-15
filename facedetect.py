import numpy as np
import cv2
import cv2.cv as cv
#from video import create_capture
from ltools.common import clock, draw_str


class FaceDetect:

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_mcs_lefteye.xml")
        self.face_sizes_list = []
        self.face_cascade

    def update(self, img):
        pass

    def detect_face(self, img):
        rects = self.face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags=cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) == 0:
            return []
        rects[:, 2:] += rects[:, :2]  #transforsms [x, y, w, h] to [x, y, x+w, y+h]

        return rects[0]

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

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

