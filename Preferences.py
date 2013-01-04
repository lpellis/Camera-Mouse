#Boa:Frame:Preferences

import cv2
import wx
from wx.lib.anchors import LayoutAnchors

def create(parent):
    return Preferences(parent)

[wxID_PREFERENCES, wxID_PREFERENCESBUTTON_CANCEL, wxID_PREFERENCESBUTTON_OK,
 wxID_PREFERENCESCHECKBOX_AUTOSTART, wxID_PREFERENCESCHOICE_EYEBROWRAISE,
 wxID_PREFERENCESCHOICE_FACE_TRACKING_CAMERA,
 wxID_PREFERENCESCHOICE_LEFTBLINK, wxID_PREFERENCESCHOICE_LEFTMOUTH,
 wxID_PREFERENCESCHOICE_LONGBLINK, wxID_PREFERENCESCHOICE_RIGHTBLINK,
 wxID_PREFERENCESCHOICE_RIGHTMOUTH, wxID_PREFERENCESNOTEBOOK1,
 wxID_PREFERENCESPANEL1, wxID_PREFERENCESPANEL2, wxID_PREFERENCESPANEL3,
 wxID_PREFERENCESSLIDER_ACCELERATION, wxID_PREFERENCESSTATICBOX1,
 wxID_PREFERENCESSTATICTEXT1, wxID_PREFERENCESSTATICTEXT2,
 wxID_PREFERENCESSTATICTEXT3, wxID_PREFERENCESSTATICTEXT4,
 wxID_PREFERENCESSTATICTEXT5, wxID_PREFERENCESSTATICTEXT6,
 wxID_PREFERENCESSTATICTEXT7, wxID_PREFERENCESSTATICTEXT8,
 wxID_PREFERENCESSTATICTEXT9,
] = [wx.NewId() for _init_ctrls in range(26)]

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
              parent=prnt, pos=wx.Point(653, 319), size=wx.Size(359, 403),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Preferences')
        self.SetClientSize(wx.Size(343, 365))
        self.Bind(wx.EVT_CLOSE, self.OnPreferencesClose)

        self.notebook1 = wx.Notebook(id=wxID_PREFERENCESNOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(344, 328), style=0)
        self.notebook1.SetFitToCurrentPage(True)
        self.notebook1.SetConstraints(LayoutAnchors(self.notebook1, True, True,
              True, True))
        self.notebook1.SetAutoLayout(True)

        self.panel1 = wx.Panel(id=wxID_PREFERENCESPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(336, 302),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT1,
              label=u'Left Blink', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 144), size=wx.Size(44, 13), style=0)

        self.panel2 = wx.Panel(id=wxID_PREFERENCESPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(336, 302),
              style=wx.TAB_TRAVERSAL)

        self.button_ok = wx.Button(id=wxID_PREFERENCESBUTTON_OK, label=u'&Ok',
              name=u'button_ok', parent=self, pos=wx.Point(176, 336),
              size=wx.Size(75, 23), style=0)
        self.button_ok.SetConstraints(LayoutAnchors(self.button_ok, False,
              False, True, True))
        self.button_ok.SetDefault()
        self.button_ok.Bind(wx.EVT_BUTTON, self.OnButton_okButton,
              id=wxID_PREFERENCESBUTTON_OK)

        self.choice_eyebrowraise = wx.Choice(choices=[],
              id=wxID_PREFERENCESCHOICE_EYEBROWRAISE,
              name=u'choice_eyebrowraise', parent=self.panel1, pos=wx.Point(192,
              208), size=wx.Size(130, 21), style=0)
        self.choice_eyebrowraise.SetSelection(0)
        self.choice_eyebrowraise.Bind(wx.EVT_CHOICE,
              self.OnChoice_eyebrowraiseChoice,
              id=wxID_PREFERENCESCHOICE_EYEBROWRAISE)

        self.staticText2 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT2,
              label=u'Right Blink', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 168), size=wx.Size(50, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT3,
              label=u'Eyebrow Raise', name='staticText3', parent=self.panel1,
              pos=wx.Point(16, 216), size=wx.Size(72, 13), style=0)

        self.button_cancel = wx.Button(id=wxID_PREFERENCESBUTTON_CANCEL,
              label=u'&Cancel', name=u'button_cancel', parent=self,
              pos=wx.Point(264, 336), size=wx.Size(75, 23), style=0)
        self.button_cancel.Bind(wx.EVT_BUTTON, self.OnButton_cancelButton,
              id=wxID_PREFERENCESBUTTON_CANCEL)

        self.staticText4 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT4,
              label=u'Long Blink (Both Eyes)', name='staticText4',
              parent=self.panel1, pos=wx.Point(16, 192), size=wx.Size(107, 13),
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
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(336, 302),
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

        self.choice_leftblink = wx.Choice(choices=[],
              id=wxID_PREFERENCESCHOICE_LEFTBLINK, name=u'choice_leftblink',
              parent=self.panel1, pos=wx.Point(192, 136), size=wx.Size(130, 21),
              style=0)
        self.choice_leftblink.Bind(wx.EVT_CHOICE, self.OnChoice_leftblinkChoice,
              id=wxID_PREFERENCESCHOICE_LEFTBLINK)

        self.choice_rightblink = wx.Choice(choices=[],
              id=wxID_PREFERENCESCHOICE_RIGHTBLINK, name=u'choice_rightblink',
              parent=self.panel1, pos=wx.Point(192, 160), size=wx.Size(130, 21),
              style=0)
        self.choice_rightblink.Bind(wx.EVT_CHOICE,
              self.OnChoice_rightblinkChoice,
              id=wxID_PREFERENCESCHOICE_RIGHTBLINK)

        self.choice_longblink = wx.Choice(choices=[],
              id=wxID_PREFERENCESCHOICE_LONGBLINK, name=u'choice_longblink',
              parent=self.panel1, pos=wx.Point(192, 184), size=wx.Size(130, 21),
              style=0)
        self.choice_longblink.Bind(wx.EVT_CHOICE, self.OnChoice_longblinkChoice,
              id=wxID_PREFERENCESCHOICE_LONGBLINK)

        self.choice_leftmouth = wx.Choice(choices=[],
              id=wxID_PREFERENCESCHOICE_LEFTMOUTH, name=u'choice_leftmouth',
              parent=self.panel1, pos=wx.Point(192, 232), size=wx.Size(130, 21),
              style=0)
        self.choice_leftmouth.Bind(wx.EVT_CHOICE, self.OnChoice_leftmouthChoice,
              id=wxID_PREFERENCESCHOICE_LEFTMOUTH)

        self.choice_rightmouth = wx.Choice(choices=[],
              id=wxID_PREFERENCESCHOICE_RIGHTMOUTH, name=u'choice_rightmouth',
              parent=self.panel1, pos=wx.Point(192, 256), size=wx.Size(130, 21),
              style=0)
        self.choice_rightmouth.Bind(wx.EVT_CHOICE,
              self.OnChoice_rightmouthChoice,
              id=wxID_PREFERENCESCHOICE_RIGHTMOUTH)

        self.staticText8 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT8,
              label=u'Left Mouth', name='staticText8', parent=self.panel1,
              pos=wx.Point(16, 240), size=wx.Size(53, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_PREFERENCESSTATICTEXT9,
              label=u'Right Mouth', name='staticText9', parent=self.panel1,
              pos=wx.Point(16, 264), size=wx.Size(59, 13), style=0)

        self.checkBox_autostart = wx.CheckBox(id=wxID_PREFERENCESCHECKBOX_AUTOSTART,
              label=u'Start automatically after reboot',
              name=u'checkBox_autostart', parent=self.panel2, pos=wx.Point(8,
              24), size=wx.Size(208, 13), style=0)
        self.checkBox_autostart.SetValue(False)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self.parent = parent;
        self._init_ctrls(parent)
        self.settings = parent.settings
        self.choice_face_tracking_camera.Clear()
        self.choice_face_tracking_camera.AppendItems([item['name'] for item in self.settings.camera_list])

        self.interface_options = [['left_click', 'Left Click'], ['right_click', 'Right Click'], ['toggle_keyboard', 'Toggle Keyboard'],
                             ['scroll_down', 'Scroll Down'], ['scroll_up', 'Scroll Up'], ['reset', 'Reset'], ['skip', '--Skip--']]
        choices = [choice[1] for choice in self.interface_options]
        self.choice_leftblink.AppendItems(choices)
        self.choice_rightblink.AppendItems(choices)
        self.choice_longblink.AppendItems(choices)
        self.choice_eyebrowraise.AppendItems(choices)
        self.choice_leftmouth.AppendItems(choices)
        self.choice_rightmouth.AppendItems(choices)

        self.load_controls()


    def load_controls(self):
        self.choice_face_tracking_camera.Select(self.parent.settings.settings['face_tracking']['camera_id'])
        self.slider_acceleration.Value = self.parent.settings.settings['face_tracking']['speed']

        self.checkBox_autostart.Value = self.parent.settings.settings['startup']['autostart']

        indices = [choice[0] for choice in self.interface_options]
        self.choice_leftblink.Select(indices.index(self.parent.settings.settings['face_tracking']['left_blink']))
        self.choice_rightblink.Select(indices.index(self.parent.settings.settings['face_tracking']['right_blink']))
        self.choice_longblink.Select(indices.index(self.parent.settings.settings['face_tracking']['long_blink']))
        self.choice_eyebrowraise.Select(indices.index(self.parent.settings.settings['face_tracking']['eyebrow_raise']))
        self.choice_leftmouth.Select(indices.index(self.parent.settings.settings['face_tracking']['left_mouth']))
        self.choice_rightmouth.Select(indices.index(self.parent.settings.settings['face_tracking']['right_mouth']))


    def OnButton_okButton(self, event):

        self.parent.settings.settings['startup']['autostart'] = self.checkBox_autostart.Value
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

    def OnChoice_eyebrowraiseChoice(self, event):
        self.parent.settings.settings['face_tracking']['eyebrow_raise'] = self.interface_options[self.choice_eyebrowraise.Selection][0]

    def OnChoice_leftblinkChoice(self, event):
        self.parent.settings.settings['face_tracking']['left_blink'] = self.interface_options[self.choice_leftblink.Selection][0]

    def OnChoice_rightblinkChoice(self, event):
        self.parent.settings.settings['face_tracking']['right_blink'] = self.interface_options[self.choice_rightblink.Selection][0]

    def OnChoice_longblinkChoice(self, event):
        self.parent.settings.settings['face_tracking']['long_blink'] = self.interface_options[self.choice_longblink.Selection][0]

    def OnChoice_leftmouthChoice(self, event):
        self.parent.settings.settings['face_tracking']['left_mouth'] = self.interface_options[self.choice_leftmouth.Selection][0]

    def OnChoice_rightmouthChoice(self, event):
        self.parent.settings.settings['face_tracking']['right_mouth'] = self.interface_options[self.choice_rightmouth.Selection][0]

