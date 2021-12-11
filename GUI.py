import Client
import UDP_Client
import wx
import threading
import time


class Panel(wx.Panel):
    current_protocol = "TCP"

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetSize(400, 400)
        # label
        self.connect_label = wx.StaticText(parent=self, label="Disconnect",
                                           pos=(30, 10))
        font = wx.Font(15, wx.FONTFAMILY_DEFAULT,
                       wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_BOLD)
        self.connect_label.SetFont(font)
        self.connect_label.SetForegroundColour(wx.Colour(255, 36, 0))

        port_text = wx.StaticText(parent=self, label="Port Number :",
                                  pos=(430, 400))
        font = wx.Font(20, wx.FONTFAMILY_SCRIPT,
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        port_text.SetFont(font)

        record_label = wx.StaticText(parent=self, label="Press the picture to start recording.",
                                     pos=(95, 610))
        font = wx.Font(12, wx.FONTFAMILY_SCRIPT,
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        record_label.SetFont(font)
        # Png
        voice_png = wx.Image('./Socket_Programming/voice_chat2.png',
                             wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, voice_png, (220, 80),
                        (voice_png.GetWidth(), voice_png.GetHeight()))
        microphone = wx.Image('./Socket_Programming/microphone.png',
                              wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.pic_button = wx.BitmapButton(self, -1, microphone, (120, 380),
                                          (microphone.GetWidth(), microphone.GetHeight()))
        self.pic_button.Bind(wx.EVT_BUTTON, self.Rec_bottom_event)
        # wx.TextCtrl(parent, id, value, pos, size, style)
        self.t1 = wx.TextCtrl(self, wx.ID_ANY, pos=(430, 460), size=(200, 20))
        lblList = ['TCP', 'UDP']
        self.RB = wx.RadioBox(
            self, label='Choose a transportation protocol', pos=(430, 500), choices=lblList, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.RB.Bind(wx.EVT_RADIOBOX, self.Protocol_choose)
        #   Client.disconnect()
        self.connect_bt = wx.Button(self, wx.ID_ANY, 'Connect', (430, 565))
        self.connect_bt.Bind(wx.EVT_BUTTON, self.LoopCond)

        self.disconnect_bt = wx.Button(
            self, wx.ID_ANY, 'DisConnect', (550, 565))
        self.disconnect_bt.Bind(wx.EVT_BUTTON, self.LoopCond)

    def Rec_bottom_event(self, event):

        threading.Thread(target=self.Record, daemon=True).start()
        self.connect_bt.Enable(False)

    def Record(self):
        self.port = self.t1.GetLineText(0)
        self.connect_label.SetLabel("Conneted")
        self.connect_label.SetForegroundColour(wx.Colour(34, 139, 34))
        if(self.current_protocol == 'TCP'):
            Client.rec(self.port)
        elif(self.current_protocol == 'UDP'):
            UDP_Client.rec(self.port)
        self.connect_label.SetLabel("DisConnected")
        self.connect_label.SetForegroundColour(wx.Colour(255, 36, 0))

    def Protocol_choose(self, event):
        self.current_protocol = self.RB.GetStringSelection()
        print(self.current_protocol)

    def connect_on_click(self):
        self.state = True
        self.port = self.t1.GetLineText(0)
        self.connect_label.SetLabel("Conneted")
        self.connect_label.SetForegroundColour(wx.Colour(34, 139, 34))
        if(self.current_protocol == 'TCP'):
            print("I am TCP")
            Client.state = True
            Client.connect(self.port)
        elif(self.current_protocol == 'UDP'):
            UDP_Client.state = True
            print("I am UDP")
            UDP_Client.connect(self.port)

    def disconnect_on_click(self):

        if(self.current_protocol == 'TCP'):
            Client.state = False
        elif(self.current_protocol == 'UDP'):
            UDP_Client.state = False
        self.connect_label.SetLabel("DisConnected")
        self.connect_label.SetForegroundColour(wx.Colour(255, 36, 0))

    def LoopCond(self, event):
        button = event.GetEventObject()
        labelName = button.GetLabel()
        # thread 目前解決方式
        # call 的 function不能是函式呼叫方式 a()
        # 而要用函式名稱,若有參數則 (target = a, args= (m,n))
        # button 點擊後用thread 去做他對應的func
        if labelName == 'Connect':
            threading.Thread(target=self.connect_on_click, daemon=True).start()
            self.connect_bt.Enable(False)
        else:
            threading.Thread(target=self.disconnect_on_click,
                             daemon=True).start()
            self.connect_bt.Enable(True)

    # def trr(self):
    #     while True:
    #         time.sleep(3)
    #         print(1)


class FrameOne(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Phone Talk")
        self.SetSize(800, 800)
        self.Center()
        panel = Panel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = FrameOne()
    app.MainLoop()
