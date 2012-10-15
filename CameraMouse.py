#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Main


modules = {u'Main': [1, 'Main frame of Application', u'Main.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Main.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)

#        self.main.SetTransparent(200)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
