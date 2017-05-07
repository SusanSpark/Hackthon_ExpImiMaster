# -*- coding: utf-8 -*-   

###########################################################################  
## Python code generated with wxFormBuilder (version Jun 30 2011)  
## http://www.wxformbuilder.org/  
##  
## PLEASE DO "NOT" EDIT THIS FILE!  
###########################################################################  

import wx
import wx.xrc
import VideoCapture
import score
from score import getScore

import time
import upload_Image
from upload_Image import onload

###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(566, 535), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"拍照", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnButton)
        # self.m_panel1.Bind(wx.EVT_IDLE,self.OnIdel)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnIdel, self.timer)

        self.cam = VideoCapture.Device()
        self.timer.Start(100)

    def OnIdel(self, event):
        # cam = VideoCapture.Device()
        self.cam.saveSnapshot('C:\\others\\temp.jpg')
        img = wx.Image("C:\\others\\temp.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        dc = wx.ClientDC(self.m_panel1)
        dc.DrawBitmap(img, 0, 0, False)

    def OnButton(self, event):
        self.cam.saveSnapshot('C:\\others\\jiaoTong University Hackthon\\ExpImiMaster\\static\\images\\savePicture\\out.jpg')
        global data
        data =onload('C:\\others\\jiaoTong University Hackthon\\ExpImiMaster\\static\\images\\savePicture\\out.jpg')
        self.Close(True)  # 关闭整个frame
        #self.timer.Destroy()
        #app.Destroy()
        event.Skip()


#if __name__ == '__main__':

def camera_oprate(num_pic,app):

    frame = MyFrame1(None)
    frame.Show(True)
    app.MainLoop()

    global data
    score=getScore(data, num_pic)

    print(score)

    return score


