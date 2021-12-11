# -*- coding: utf-8 -*-

import pyaudio
import socket
import sys
import tkinter
import wx
import threading
from PIL import Image, ImageTk

po = tkinter.Tk()

chunk = 1024
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=10240,
                output=True)

host = "127.0.0.1"
port = 50020
backlog = 5
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def create_label_image():
    img = Image.open('./Socket_Programming/server.png')
# 讀取圖片

    img = img.resize((img.width-10, img.height-10))
# 縮小圖片

    imgTk = ImageTk.PhotoImage(img)
# 轉換成Tkinter可以用的圖片

    lbl_2 = tkinter.Label(po, image=imgTk)
    # lbl_port =
# 宣告標籤並且設定圖片
    lbl_2.image = imgTk

    lbl_2.pack()


class listen(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        s.listen(backlog)
        client, address = s.accept()
        while True:
            data = client.recv(size)
            if data:
                stream.write(data)
                client.send("ACK".encode())


po.title("Server")
po.geometry('500x500')
start_bt = tkinter.Button(po, width=20, height=4, text='Start', bg="#227700",
                          command=lambda: listen(), fg='black')
exit_bt = tkinter.Button(po, width=20, height=4, text='Exit',
                         bg="#CC0000", command=po.destroy)

labelA = tkinter.Label(po, text="Host : 127.0.0.1",
                       fg="black", font=('Arial', 20))
labelB = tkinter.Label(po, text="Port : 50020",
                       fg="black", font=('Arial', 20))

labelA.pack()
labelB.pack()
start_bt.pack()
exit_bt.pack()
labelA.place(x=150, y=300)
labelB.place(x=170, y=340)
start_bt.place(x=25, y=400)
exit_bt.place(x=325, y=400)
create_label_image()
po.mainloop()

stream.close()
p.terminate()

# TODO Server端 變沒有中斷連線 無法再次連接 in TCP
