#Boa:Frame:Frame1

import wx
import Preferences
import cv2
import ltools.image
import ltools.convert
import Image
import facedetect

t = cv2.VideoCapture(0)



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON_SETTINGS, wxID_FRAME1PANEL_CAMERA,
 wxID_FRAME1PANEL_MAIN,
] = [wx.NewId() for _init_ctrls in range(4)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(552, 349), size=wx.Size(431, 234),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Camera Mouse')
        self.SetClientSize(wx.Size(415, 196))
        self.SetWindowVariant(wx.WINDOW_VARIANT_NORMAL)
        self.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)

        self.panel_main = wx.Panel(id=wxID_FRAME1PANEL_MAIN, name=u'panel_main',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(415, 196),
              style=wx.TAB_TRAVERSAL)

        self.panel_camera = wx.Panel(id=wxID_FRAME1PANEL_CAMERA,
              name=u'panel_camera', parent=self.panel_main, pos=wx.Point(16,
              16), size=wx.Size(200, 160), style=wx.TAB_TRAVERSAL)
        self.panel_camera.SetBackgroundColour(wx.Colour(240, 240, 200))

        self.button_settings = wx.Button(id=wxID_FRAME1BUTTON_SETTINGS,
              label=u'&Settings..', name=u'button_settings',
              parent=self.panel_main, pos=wx.Point(224, 152), size=wx.Size(75,
              23), style=0)
        self.button_settings.Bind(wx.EVT_BUTTON, self.OnButton_settingsButton,
              id=wxID_FRAME1BUTTON_SETTINGS)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.preferences = Preferences.create(self)
        self.Bind(wx.EVT_IDLE, self.on_idle)
        self.Timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Timer.Start(30) # required to trigger the on_idle..
        self.FaceDector = facedetect.FaceDetect()
        print 'done'


    def on_idle(self, event):
        ret, frame = t.read()
        dc = wx.ClientDC(self.panel_camera)  #320x240
        h, w, d = frame.shape
        frame = cv2.resize(frame, (200, int(200. / w * h)))
        h, w, d = frame.shape
        frame = ltools.image.convert_to_grayscale(frame)
        print self.FaceDector.detect_face(frame)

        dc.DrawBitmap(ltools.convert.numpyToBitmap(frame), 10, 10, False)
        print 'idle'

    def OnTimer(self, event):
        pass
        #print ltools.convert.numpyToBitmap(frame)


    def OnButton_settingsButton(self, event):
        self.preferences.Show()
        event.Skip()
