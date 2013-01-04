#Boa:Frame:Preferences

import cv2
import wx
from wx.lib.anchors import LayoutAnchors

def create(parent):
    return Preferences(parent)

[wxID_PREFERENCES, wxID_PREFERENCESBUTTON_CANCEL, wxID_PREFERENCESBUTTON_OK,
 wxID_PREFERENCESCHOICE1, wxID_PREFERENCESCHOICE2,
 wxID_PREFERENCESCHOICE_FACE_TRACKING_CAMERA, wxID_PREFERENCESNOTEBOOK1,
 wxID_PREFERENCESPANEL1, wxID_PREFERENCESPANEL2, wxID_PREFERENCESPANEL3,
 wxID_PREFERENCESSLIDER_ACCELERATION, wxID_PREFERENCESSTATICBOX1,
 wxID_PREFERENCESSTATICTEXT1, wxID_PREFERENCESSTATICTEXT2,
 wxID_PREFERENCESSTATICTEXT3, wxID_PREFERENCESSTATICTEXT4,
 wxID_PREFERENCESSTATICTEXT5, wxID_PREFERENCESSTATICTEXT6,
 wxID_PREFERENCESSTATICTEXT7,
] = [wx.NewId() for _init_ctrls in range(19)]

class Preferences(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId= -1, page=self.panel1, select=True,
              text=u'Face Tracking')
        parent.AddPage(imageId= -1, page=self.panel2, select=False,
              text=u'Startup')
        parent.AddPage(imageId= -1, page=self.panel3, select=False,
              text=u'Iris Tracking')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PREFERENCES, name=u'Preferences',
              parent=prnt, pos=wx.Point(704, 325), size=wx.Size(358, 373),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Preferences')
        self.SetClientSize(wx.Size(342, 335))
        self.Bind(wx.EVT_CLOSE, self.OnPreferencesClose)

        self.notebook1 = wx.Notebook(id=wxID_PREFERENCESNOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(344, 296), style=0)
        self.notebook1.SetFitToCurrentPage(True)
        self.notebook1.SetConstraints(LayoutAnchors(self.notebook1, True, True,
              True, True))
        self.notebook1.SetAutoLayout(True)

        self.panel1 = wx.Panel(id=wxID_PREFERENCESPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(336, 270),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT1,
              label=u'Left Blink', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 144), size=wx.Size(44, 13), style=0)

        self.panel2 = wx.Panel(id=wxID_PREFERENCESPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(336, 270),
              style=wx.TAB_TRAVERSAL)

        self.button_ok = wx.Button(id=wxID_PREFERENCESBUTTON_OK, label=u'&Ok',
              name=u'button_ok', parent=self, pos=wx.Point(176, 304),
              size=wx.Size(75, 23), style=0)
        self.button_ok.SetConstraints(LayoutAnchors(self.button_ok, False,
              False, True, True))
        self.button_ok.SetDefault()
        self.button_ok.Bind(wx.EVT_BUTTON, self.OnButton_okButton,
              id=wxID_PREFERENCESBUTTON_OK)

        self.choice1 = wx.Choice(choices=['Left Click', 'Right Click',
              'Toggle Keyboard', '--Ignore--'], id=wxID_PREFERENCESCHOICE1,
              name='choice1', parent=self.panel1, pos=wx.Point(136, 232),
              size=wx.Size(130, 21), style=0)
        self.choice1.SetSelection(0)

        self.choice2 = wx.Choice(choices=[], id=wxID_PREFERENCESCHOICE2,
              name='choice2', parent=self.panel2, pos=wx.Point(168, 88),
              size=wx.Size(130, 21), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT2,
              label=u'Right Blink', name='staticText2', parent=self.panel1,
              pos=wx.Point(8, 176), size=wx.Size(50, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT3,
              label=u'Eyebrow Raise', name='staticText3', parent=self.panel1,
              pos=wx.Point(16, 232), size=wx.Size(72, 13), style=0)

        self.button_cancel = wx.Button(id=wxID_PREFERENCESBUTTON_CANCEL,
              label=u'&Cancel', name=u'button_cancel', parent=self,
              pos=wx.Point(264, 304), size=wx.Size(75, 23), style=0)
        self.button_cancel.Bind(wx.EVT_BUTTON, self.OnButton_cancelButton,
              id=wxID_PREFERENCESBUTTON_CANCEL)

        self.staticText4 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT4,
              label=u'Long Blink (Both Eyes)', name='staticText4',
              parent=self.panel1, pos=wx.Point(8, 200), size=wx.Size(107, 13),
              style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_PREFERENCESSTATICBOX1,
              label=u'Pointer Acceleration', name='staticBox1',
              parent=self.panel1, pos=wx.Point(16, 48), size=wx.Size(304, 72),
              style=0)
        self.staticBox1.Enable(True)

        self.slider_acceleration = wx.Slider(id=wxID_PREFERENCESSLIDER_ACCELERATION,
              maxValue=100, minValue=0, name=u'slider_acceleration',
              parent=self.panel1, pos=wx.Point(80, 80), size=wx.Size(160, 24),
              style=wx.SL_HORIZONTAL, value=60)
        self.slider_acceleration.SetLabel(u'')
        self.slider_acceleration.Enable(True)
        self.slider_acceleration.Bind(wx.EVT_COMMAND_SCROLL,
              self.OnSlider_accelerationCommandScroll,
              id=wxID_PREFERENCESSLIDER_ACCELERATION)

        self.staticText5 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT5,
              label=u'Slow', name='staticText5', parent=self.panel1,
              pos=wx.Point(32, 80), size=wx.Size(23, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT6,
              label=u'Fast', name='staticText6', parent=self.panel1,
              pos=wx.Point(256, 80), size=wx.Size(22, 13), style=0)

        self.panel3 = wx.Panel(id=wxID_PREFERENCESPANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(336, 270),
              style=wx.TAB_TRAVERSAL)

        self.choice_face_tracking_camera = wx.Choice(choices=['testclass1'],
              id=wxID_PREFERENCESCHOICE_FACE_TRACKING_CAMERA,
              name=u'choice_face_tracking_camera', parent=self.panel1,
              pos=wx.Point(104, 13), size=wx.Size(216, 21), style=0)
        self.choice_face_tracking_camera.Bind(wx.EVT_CHOICE,
              self.OnChoice_face_tracking_camera,
              id=wxID_PREFERENCESCHOICE_FACE_TRACKING_CAMERA)

        self.staticText7 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT7,
              label=u'Camera', name='staticText7', parent=self.panel1,
              pos=wx.Point(24, 16), size=wx.Size(38, 13), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self.parent = parent;
        self._init_ctrls(parent)
        self.settings = parent.settings
        self.choice_face_tracking_camera.Clear()
        self.choice_face_tracking_camera.AppendItems([item['name'] for item in self.settings.camera_list])
        self.load_controls()


    def load_controls(self):
        self.choice_face_tracking_camera.Select(self.parent.settings.settings['face_tracking']['camera_id'])
        self.slider_acceleration.Value = self.parent.settings.settings['face_tracking']['speed']


    def OnButton_okButton(self, event):
        self.parent.settings.save()
        self.Hide()


    def OnButton_cancelButton(self, event):

        self.parent.settings.apply_settings(self.parent.settings.defaults)
        self.load_controls()
        self.Hide()

    def OnPreferencesClose(self, event):
        self.Hide()

    def OnChoice_face_tracking_camera(self, event):

        self.parent.settings.load_face_tracking_camera(self.choice_face_tracking_camera.Selection)
        print self.choice_face_tracking_camera.Selection
        print 'Selecting camera'

    def OnSlider_accelerationCommandScroll(self, event):
        self.parent.settings.settings['face_tracking']['speed'] = self.slider_acceleration.Value
        event.Skip()

