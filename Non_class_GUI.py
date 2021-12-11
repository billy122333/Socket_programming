# see the tutorial at https://pythonspot.com/wxpython-window/
# install instaltion manager pip in VS
# (1) download get-pip.py at https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# (2) run get-pip.py scripy in VScode
# (3) you migh have to add script directory " "  to path (從控制台==>系統==>進階系統設定 ==>環境變數==>Path 變數加入 C:/Users/Liu/AppData/Local/Programs/Python/Python38-32/)
# install the library wxPython using "pip install -U wxPython" in console
# build the app with a frame with the stucture below
import Client
import UDP_Client
import wx
import threading
import time

# import Client

current_protocol = "TCP"

# class Main_Frame(wx.Frame):
# creating an app
app = wx.App()
# creating a frame with 'win.py as the caption of the frame '
frame = wx.Frame(None, -1, 'Server.py')


# panel
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetSize(400, 400)

# statictext
connect_label = wx.StaticText(parent=panel, label="Disconnect",
                              pos=(30, 10))
font = wx.Font(15, wx.FONTFAMILY_DEFAULT,
               wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_BOLD)
connect_label.SetFont(font)
connect_label.SetForegroundColour(wx.Colour(255, 36, 0))

port_text = wx.StaticText(parent=panel, label="Port Number :",
                          pos=(430, 400))
font = wx.Font(20, wx.FONTFAMILY_SCRIPT,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
port_text.SetFont(font)

record_label = wx.StaticText(parent=panel, label="Press the picture to start recording.",
                             pos=(95, 610))
font = wx.Font(12, wx.FONTFAMILY_SCRIPT,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
record_label.SetFont(font)

# Png
voice_png = wx.Image('C:\\Users\\User\\Desktop\\python\\Socket_Programming\\voice_chat2.png',
                     wx.BITMAP_TYPE_ANY).ConvertToBitmap()
wx.StaticBitmap(panel, -1, voice_png, (220, 80),
                (voice_png.GetWidth(), voice_png.GetHeight()))


def Record(event):
    global current_protocol
    port = t1.GetLineText(0)
    if(current_protocol == 'TCP'):
        Client.rec(port)
    elif(current_protocol == 'UDP'):
        UDP_Client.rec(port)


microphone = wx.Image('C:\\Users\\User\\Desktop\\python\\Socket_Programming\\microphone.png',
                      wx.BITMAP_TYPE_ANY).ConvertToBitmap()
pic_button = wx.BitmapButton(panel, -1, microphone, (120, 380),
                             (microphone.GetWidth(), microphone.GetHeight()))
pic_button.Bind(wx.EVT_BUTTON, Record)

# wx.TextCtrl(parent, id, value, pos, size, style)

t1 = wx.TextCtrl(panel, wx.ID_ANY, pos=(430, 460), size=(200, 20))


# radiobox


def Protocol_choose(event):
    global current_protocol
    current_protocol = RB.GetStringSelection()
    print(current_protocol)


lblList = ['TCP', 'UDP']
RB = wx.RadioBox(
    panel, label='Choose a transportation protocol', pos=(430, 500), choices=lblList, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
RB.Bind(wx.EVT_RADIOBOX, Protocol_choose)


# botton


def LoopCond(event):
    button = event.GetEventObject()
    labelName = button.GetLabel()
    if labelName == 'Connect':
        threading.Thread(target=connect_on_click, daemon=True).start()
        connect_bt.Enable(False)
    else:
        threading.Thread(target=disconnect_on_click, daemon=True).start()
        connect_bt.Enable(True)
        #parent_frame = self.GetParent()
        # parent_frame.Close()


def connect_on_click():
    port = t1.GetLineText(0)

    if(current_protocol == 'TCP'):
        print("I am TCP")
        Client.connect(port)
    elif(current_protocol == 'UDP'):
        print("I am UDP")
        target = UDP_Client.connect(port)


def disconnect_on_click():

    connect_label.SetLabel("DisConnected")
    connect_label.SetForegroundColour(wx.Colour(255, 36, 0))


#   Client.disconnect()
connect_bt = wx.Button(panel, wx.ID_ANY, 'Connect', (430, 565))
connect_bt.Bind(wx.EVT_BUTTON, LoopCond)

disconnect_bt = wx.Button(panel, wx.ID_ANY, 'DisConnect', (550, 565))
disconnect_bt.Bind(wx.EVT_BUTTON, disconnect_on_click)

frame.SetSize(800, 800)
frame.Center()
frame.Show()
app.MainLoop()
